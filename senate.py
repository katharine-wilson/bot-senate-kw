import os
import json
import requests
from bs4 import BeautifulSoup

url = "https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_1.xml"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    xml_content = response.content
else:
    print("Failed to retrieve the XML file.")
    exit()

soup = BeautifulSoup(xml_content, features='xml')
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
    description = vote.find('title').text

    # Track the highest vote number and store the most recent vote details
    if number > latest_vote_number:
        latest_vote_number = number
        most_recent_vote = [number, date, question, issue, yeas, nays, description]  # Store the most recent vote details

# Load previous vote number from a file (if exists)
previous_vote_file = 'previous_vote.json'

if os.path.exists(previous_vote_file):
    with open(previous_vote_file, 'r') as file:
        previous_vote_data = json.load(file)
        previous_vote_number = previous_vote_data.get('latest_vote_number', 0)  # Get previous vote number
else:
    previous_vote_number = 0  # Default if no file exists

# Compare the latest vote number with the previous vote number
if latest_vote_number > previous_vote_number:
    update = "Found a new Senate vote."
    
    # Prepare detailed update message for the most recent vote
    if most_recent_vote:
        update += f"\nNew Senate vote {most_recent_vote[1]}: {most_recent_vote[2]} for {most_recent_vote[3]}. The yeas were {most_recent_vote[4]} and the nays were {most_recent_vote[5]}. Description: {most_recent_vote[6]}"
        
    # Save the latest vote number for future comparisons
    with open(previous_vote_file, 'w') as file:
        json.dump({'latest_vote_number': latest_vote_number}, file)
else:
    update = "No new votes found."

print(update)