#!/usr/bin/env python
import sys
import os
import random
from twython import Twython

CONSUMER_KEY = 'Your-Consumer-Key'
CONSUMER_SECRET = 'Your-Secret-Key'
ACCESS_KEY = 'Your-Access-Key'
ACCESS_SECRET = 'Your-Access-Secret'

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

def randomTweet():
    try:
        tweetsFile = open(os.path.join(__location__,'tweets.txt'),'r')
        tweetsList = tweetsFile.readlines()
        tweetsFile.close()
        randomChoice = random.randrange(len(tweetsList))
        print (tweetsList[randomChoice]) #For debugging only
        api.update_status(status=tweetsList[randomChoice])
        return None
    except IOError:
        return None 
		
randomTweet()
