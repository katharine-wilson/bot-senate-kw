# bot-senate-kw
### April 5 Memo 

For this project, where I made a slack bot that alerts every time there is a new vote recorded in the Senate, my process was to build each step one at a time. First, I found the best file to scrape from the Senate website, an xml file. Then, I scraped the website for each part of the vote information that I wanted to include in my alert. After that was done, I asked TerpAI how to limit its responses to just the most recent vote in the Senate. I ended up with a system that recorded the most recent vote number and only alerted information for vote numbers higher than the most recent vote number already recorded before the bot last ran. I then connected the code with a slack channel and scheduled the bot to run every five minutes. 

The bot has ended up exactly how I wanted it. It’s a quick, easy to understand, alert bot that will notify me when the U.S. Senate has taken a vote, its outcome, and what the vote was on. This bot fills a crucial gap for congressional reporters who find it difficult to track the Senate in the same way they cover the House (which has an app run by the Democratic Whip which essentially performs this same service). I like how simple the alert system is to view and understand. 

I decided that I don’t need to store this data anywhere for the bot’s current purpose. The bot’s usefulness comes from simply alerting me to a new vote in the U.S. Senate, but the record of these votes is available in other places. If I wanted to eventually make a bot that analyzes how the Senate votes and what they’re voting on, I would have to store the data. This could look like a news app that breaks down all the votes in the Senate into the categories: nominations, cloture, amendments and bill votes. An eventual news app could also use AI to add categories for what type of issue each vote addresses (such as immigration, staffing, funding etc.). 

If the bot was able to accept input from users, it could give more detail about the vote. For example, I could somehow link the bot with another Senate website to give the list of how each senator voted. Ideally, it would highlight senators that voted with their opposing party. I would also like the bot to provide a link to the full text of the legislation from congress.gov. 

A more useful version of this bot would pull from multiple sources of Senate data to provide more information about each vote and what it does. The bot could identify lead senate sponsors of bills, previous roll call vote information and the party breakdown of Senators voting for and against each vote. 



### March 28 Update
I feel like I'm really close on this one. When I run it inside codespaces it runs every minute, updates correctly, etc. But, I can't seem to get it to print on slack. I think it's some small problem with the slack part of it, becuase I keep checking the slack related code and I can't find anything missing. 

Since my last bot update I have connected the bot to the senate vote recording website, made an udpate sentence with key information on the vote, and input the code to set the bot up to slack. I also was able to code the bot so it updated every time there is a new vote, and only show the new vote, instead of listing all of the votes. 

I have learned that there are a lot of easy ways to mess this project up. Everytime I put in a new line of code, there are new errors about missing packages, messed up lines and more. I have also learned that this set of data is really well set up for a slack bot and is consistantly update without any weird coding mistakes. 

If I could, I would have tried to set up the slack bot part of this first before I coded the rest, because now I'm just worried I'll mess up the meat of my code by messing around with my slack problem. 



### earlier update
I'm planning on making a bot that notifies me every time an action (vote or rule vote) is take non a bill in the U.S. Senate. 

To do this, I will get information from congressional APIs (https://api.congress.gov/#/bill/bill_actions specifically the /bill/{congress}/{billType}/{billNumber}/actions request). 

I would filter to only get information from the Senate chamber and the types of actions I'm interested in (rule vote, passed, failed, signed by president). 

So far, I have made a rough outline for the code for the slack bot. I also added the Senate API key to my secrets section. My next steps would be looking at the different options given by the api key and filling in the blanks in my code. Also, I need to set this up in slack. 

However, now that I've set this up, I'm unsure if this api method is best for the information I want to grab. This website https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_1.htm might actually give me more of what I'm looking for. But, I'm unsure of how to grab it for this project. 