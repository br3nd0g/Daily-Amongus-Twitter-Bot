import tweepy
import os
import letterGetter as lg
import generateImage as gi
#import discordPoster as dp
import random
import time

consumerSecret = os.environ['consumer_keySecret']
consumerKey = os.environ['consumer_key']
accessTokenSecret = os.environ['access_tokenSecret']
accessToken = os.environ['access_token']

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

adjectiveArray, nounArray, verbArray = lg.letterArrays()

sentence = f"the {random.choice(adjectiveArray)} impostor used a {random.choice(nounArray)} to {random.choice(verbArray)}".upper()

gi.generateImage(sentence)

#dp.runAmongBot()

while True:
  print(f"posted amongus at {time.asctime(time.localtime())}")
  api.update_status_with_media("", "currentAmong.png")
  time.sleep(14400)