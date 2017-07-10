#!/usr/bin/python

import yaml
import os
import sys
from time import sleep
from slackclient import SlackClient
from random import randint

import requests

# Initializes variables
def init():
    config_file = os.getcwd() + '/clever.yml'
    config = yaml.safe_load(open(config_file))
    global username
    username = config['bot_name']
    global channel
    channel = config['channel']
    global sc
    sc = SlackClient(config['slack_api_token'])
    global channel_id
    channel_id = getChannelId(channel)
    ## Cleverbot specific
    global cb_url
    cb_url = "https://www.cleverbot.com/getreply"
    global cb_key
    cb_key = config['cleverbot_key']
    global reply_factor
    reply_factor = config['reply_factor']


#Logs message TODO for now prints to console
def log(message, obj = None):
    print(message);
    if not obj == None:
        print(obj)


# Exit the program
def die(message = None, e = None):
    log(message, e);
    sys.exit();
# Gets channel id as part of init process
def getChannelId(channel_name):
    api_call = sc.api_call(
        "chat.postMessage",
        channel=channel_name,
        text="I am the username! I will be listening on this channel. Type `@username help` for more info".replace("username", username) ,
        username=username
    )
    if api_call['ok']:
        return api_call['channel']
    else:
        exit("Failed to get channel ID for channel" + channel, api_call)

# Sends message to slack channel
def sendMsg(msgToSend):
    sc.api_call(
        "chat.postMessage",
        channel=channel,
        text=msgToSend,
        username=username
    )

# Returns help message
def getHelpMessage():
    message = """I am the username! I will reply to all the messages tagged with @username. 
    Additional commands are
    `@username help` prints this
    `@username die` exits
    `@username your name is <name>` TODO change bot name" 
    """.replace("username", username)
    return message;

#Parses slack messages and replys
def handleMessage(message):
    log("Asked:" + message)
    if u"@%s help" % (username) in event[0]["text"]:
        reply = getHelpMessage()
    elif  u"@%s die" % (username) in event[0]["text"]:
        sendMsg("Dead")
        die("Exit")
    elif username in message:
        reply = askCleverBot(message.replace(username, "").replace("@",""))
        log("REPLIED:" + reply)
    #Replys to a message randomly when username isn't mentioned in the message
    elif reply_factor != 0 and reply_factor > randint(1, 100):
        reply = askCleverBot(message)
    if not reply == None:
        log("Replied:" + message)
        sendMsg(reply);


# Connects to cleverbot to ask a question
def askCleverBot(message):
    params = {
        "input": message,
        "key": cb_key,
        "conversation_id": channel,
    }

    try:
        r = requests.get(cb_url, params=params)
    # catch errors, print then exit.
    except requests.exceptions.RequestException as e:
        print(e)
    return r.json()["output"]


init();

if sc.rtm_connect():
 while True:
     event=sc.rtm_read()
     if not event ==[]:
         if event[0]["type"]=="message" and channel_id == event[0]["channel"]:
             # prevents endless loop of replying to itself
             if "username" in event[0] and event[0]["username"] == username:
                 continue
             # handler
             handleMessage(event[0]["text"])
     sleep(.3)
