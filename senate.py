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

for vote in votes:
    date = vote.find('vote_date').text
    question = vote.find('question').text
    issue = vote.find('issue').text
    yeas = vote.find('yeas').text
    nays = vote.find('nays').text

update = f"New Senate vote {date}: {question} for [issue]. The yeas were [yeas] and the nays were [nays]. "

print(update)