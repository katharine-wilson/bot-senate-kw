import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json
import requests
from bs4 import BeautifulSoup

slack_token = os.environ.get('SLACK_API_KEY')
client = WebClient(token=slack_token)

def fetch_votes():
    url = "https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_1.xml"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        return response.content
    else:
        print("Failed to retrieve the XML file.")
        return None

def parse_votes(xml_content):
    soup = BeautifulSoup(xml_content, 'lxml-xml')
    votes = soup.find_all('vote')

    most_recent_vote = None  # Variable to store the most recent vote
    latest_vote_number = 0  # Variable to track the highest vote number

    for vote in votes:
        date = vote.find('vote_date').text
        question = vote.find('question').text
        issue = vote.find('issue').text
        yeas = vote.find('yeas').text
        nays = vote.find('nays').text
        number = int(vote.find('vote_number').text)
        full_title = vote.find('title').text

        if ';' in full_title:
            description = full_title.split(';', 1)[1].strip()
        else:
            description = full_title.strip()

        # Track the highest vote number and store the most recent vote details
        if number > latest_vote_number:
            latest_vote_number = number
            most_recent_vote = [number, date, question, issue, yeas, nays, description]  # Store the most recent vote details

    return most_recent_vote, latest_vote_number

def load_previous_vote_number():
    previous_vote_file = 'previous_vote.json'
    if os.path.exists(previous_vote_file):
        with open(previous_vote_file, 'r') as file:
            previous_vote_data = json.load(file)
            return previous_vote_data.get('latest_vote_number', 0)  # Get previous vote number
    else:
        return 0  # Default if no file exists

def save_latest_vote_number(latest_vote_number):
    with open('previous_vote.json', 'w') as file:
        json.dump({'latest_vote_number': latest_vote_number}, file)

def main():
    xml_content = fetch_votes()
    if xml_content:
        most_recent_vote, latest_vote_number = parse_votes(xml_content)
        previous_vote_number = load_previous_vote_number()

        # Compare the latest vote number with the previous vote number
        if latest_vote_number > previous_vote_number:
            update = "Found a new Senate vote."
            # Prepare detailed update message for the most recent vote
            if most_recent_vote:
                    update += f"\nOn {most_recent_vote[1]} the Senate voted on {most_recent_vote[3]}. The yeas were {most_recent_vote[4]} and the nays were {most_recent_vote[5]}. {most_recent_vote[6]}, Vote: {most_recent_vote[2]}"
                
            print(update)

            try:
                response = client.chat_postMessage(
                    channel="slack-bots",
                    text=update,
                    unfurl_links=True, 
                    unfurl_media=True
                )
                print("success!")
            except SlackApiError as e:
                print(f"Got an error: {e.response['error']}")
              
            save_latest_vote_number(latest_vote_number)  # Save the latest vote number

        else:
            print("No new votes found.")

if __name__ == "__main__":
    main()
