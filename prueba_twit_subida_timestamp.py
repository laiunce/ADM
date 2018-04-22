#!/usr/bin/env python
# visit https://www.childs.be/blog/post/how-to-run-a-python-script-as-a-service-in-background-as-a-daemon for instructions
# uses https://raw.githubusercontent.com/metachris/python-posix-daemon/master/src/daemon2x.py
from __future__ import print_function
import time, sys, logging
import tweepy
import datetime
import json
from elasticsearch import Elasticsearch
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Logging
logging.basicConfig(    filename='/var/log/daemon_escucha_twitter.log',
                        filemode='a',
                        format='[%(asctime)s] %(message)s',
                        datefmt='%Y/%d/%m %H:%M:%S',
                        level=logging.INFO)

#telnet  27017 
WORDS = ['noche']


CONSUMER_KEY = '0LIjneGg3swyWkghj0VXMaTc8'
CONSUMER_SECRET = 'IU7ce8BATcqHVVH96dF2JciTrPZYjBEjD82mgc1AKmI2SI0hTw'
ACCESS_TOKEN = '859113296112357377-pj5hxFyQcP0N31JvXVpChs4ur87jdIS'
ACCESS_TOKEN_SECRET = 'bEQ7rbGqojHbef9kkzYB8BRaRmoqXG2aUMk1B0Dwv7bvy'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


user,passw = 'laiun.ce@gmail.com','Lw8dyr15'

ES_HOST = 'https://search-adm-35ohesxnchgmztcblylrwe3dvu.us-east-1.es.amazonaws.com'
es = Elasticsearch(ES_HOST,  verify_certs=False)




class StreamListener(tweepy.StreamListener): 



    #This is a class provided by tweepy to access the Twitter Streaming API. 
 
    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")
 
    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False
 
    def on_data(self, data):
        #This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:

    
            # Decode the JSON from Twitter

            datajson = json.loads(data)
            #datajson['datetime'] = str(datetime.datetime.now())
            datajson['datetime_key'] = datetime.datetime.now()


            #print out a message to the screen that we have collected a tweet

            go = es.create(index="twitter3",
                      doc_type="bajada_twitter3",
                      id=datajson['id'],
                      body=datajson
                     )

            print (json.dumps(go))

            
            #insert the data into the mongoDB into a collection called twitter_search
            #if twitter_search doesn't exist, it will be created.
            #db.twitter_search.insert(datajson)
        except Exception as e:
           print(e)


logging.info('--------------')
logging.info(time.strftime("%I:%M:%S %p"))
logging.info('Daemon Started')
while True:
        #Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
        listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) 
        streamer = tweepy.Stream(auth=auth, listener=listener)
        print("Tracking: " + str(WORDS))
        streamer.filter(track=WORDS)
logging.info(time.strftime("%I:%M:%S %p"))
logging.info('Daemon Ended')


twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
stream = twitter_stream.statuses.filter(locations=[-6.38,49.87,1.77,55.81])




