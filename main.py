# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
import time
import threading
import base64
import requests
import json
import requests
import urllib.request
from bs4 import BeautifulSoup

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACfe5457f839425b24d9f237064c4fc777", "4dd1381fa108f3770977993e6dacfb68")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
def textme(nfltext):
    client.messages.create(to="+12533142238", 
                        from_="+12063393503", 
                        body=nfltext)

# for i in range(1):
#     time.sleep(10)
#     textme()
#     time.sleep(20)
#     print('Tock')

# def api_call(player):

# last_update = ""

def cycle():
    threading.Timer(1200.0, cycle).start() # called every 20 minutes
    last_update = 0
    players = ["RodgAa", "TrubMi"]
    for player in players:
        url = f'https://www.pro-football-reference.com/players/R/{player}00/gamelog/2018/'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html5lib")
        yds = soup.findAll("td", {"data-stat": "pass_yds"})[0].string
        tds = soup.findAll("td", {"data-stat": "pass_td"})[0].string
        opp = soup.findAll("td", {"data-stat": "opp"})[0].string
        if(last_update != yds):
            last_update = yds
            print(player + " had " + yds + " yards and " + tds + " TD's vs " + opp)
            textme(player + " had " + yds + " yards and " + tds + "TD's vs " + opp)
        else:
            cycle()
cycle()


