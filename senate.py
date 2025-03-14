import os
import json
import requests
from slack import WebClient
from slack.errors import SlackApiError


SenateKey = "CONGRESS_API_KEY"

url = f"https://api.congress.gov/v3/bill/117/hr/3076/actions?api_key=[SenateKey]"

update = f"Update to [bill title/number]: The Senate [passed/failed] a vote on [rule/passage]. To view vote count and text: [url]"

msg = update
try:
    response = client.chat_postMessage(
        channel="slack-bots",
        text=msg,
        unfurl_links=True, 
        unfurl_media=True
    )
    print("success!")
except SlackApiError as e:
    assert e.response["ok"] is False
    assert e.response["error"]
    print(f"Got an error: {e.response['error']}")