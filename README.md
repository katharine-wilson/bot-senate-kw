# bot-senate-kw

I'm planning on making a bot that notifies me every time an action (vote or rule vote) is take non a bill in the U.S. Senate. 

To do this, I will get information from congressional APIs (https://api.congress.gov/#/bill/bill_actions specifically the /bill/{congress}/{billType}/{billNumber}/actions request). 

I would filter to only get information from the Senate chamber and the types of actions I'm interested in (rule vote, passed, failed, signed by president). 

So far, I have made a rough outline for the code for the slack bot. I also added the Senate API key to my secrets section. My next steps would be looking at the different options given by the api key and filling in the blanks in my code. Also, I need to set this up in slack. 

However, now that I've set this up, I'm unsure if this api method is best for the information I want to grab. This website https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_1.htm might actually give me more of what I'm looking for. But, I'm unsure of how to grab it for this project. 