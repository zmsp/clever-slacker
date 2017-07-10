

This bot replies to messages using cleverbot api in a given slack channel. 

# What can it do?
* Checks if a host is up or down using ping
* Replies to messages using cleverbot api
* More features to be added.


# Requirements
* Python 2.7 environment
* yaml, slackclient and requests Python packages installed

# Variables
```
slack_api_token: "XXXX" #Get it form https://api.slack.com/custom-integrations/legacy-tokens
cleverbot_key: "XXXX" # Get it from https://www.cleverbot.com/api/my-account/
log_file: "./clever.log" # Location to log TODO
bot_name: "Machine" #The name bot response to
emoji: ":robot_face:" # TODO
channel: "#api-test" #Channel Namen
reply_factor: 10 # % of messages to reply to when bot username isn't in the message
```

# Setting up
* Clone this repository
* Setup variables on clever.yml file. See Variables for details
* Run python ./clever.py

# Use
After running, you should see a help message printed on the slack channel. You can interect with bot by writing bot name on the message.  
Example: if the bot name is Machine, you can ask 

```
@Machine what is 1+1
Machine:2.
OR
Machine roll dice
Machine:I got a three.
OR
@Machine ping google.com
Machine: google.com is up!
```

![Alt text](/screenshot.png?raw=true "I am the Machine")


# Data/Privacy Policy
Replies generated through cleverbot api. Read cleverbot's privacy policy here: http://www.cleverbot.com/privacy
