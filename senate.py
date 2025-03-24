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

soup = BeautifulSoup(xml_content, features = 'xml')
votes = soup.find_all('vote')

most_recent = []

for vote in votes:
    date = vote.find('vote_date').text
    question = vote.find('question').text
    issue = vote.find('issue').text
    yeas = vote.find('yeas').text
    nays = vote.find('nays').text
    number = vote.find('vote_number').text

    if number > '00134': most_recent.append (soup)

update = f"New Senate vote {most_recent['date']}: {most_recent['question']} for {most_recent['issue']}. The yeas were {most_recent['yeas']} and the nays were {most_recent['nays']}. "

print(update)