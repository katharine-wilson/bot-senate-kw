# bot-senate-kw
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