# bot-senate-kw

I'm planning on making a bot that notifies me every time an action (vote or rule vote) is take non a bill in the U.S. Senate. 

To do this, I will get information from congressional APIs (https://api.congress.gov/#/bill/bill_actions specifically the /bill/{congress}/{billType}/{billNumber}/actions request). 

I would filter to only get information from the Senate chamber and the types of actions I'm interested in (rule vote, passed, failed, signed by president). 

So far, I have made a rough outline for the code for the slack bot. 