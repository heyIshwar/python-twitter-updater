import time, os, tweepy, wikiquotes
from textblob import TextBlob
from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

time_interval = int(input("Time in second to tweet gandhi quote: "))

i = 1

while True:
	api.update_status(wikiquotes.random_quote("gandhi", "english")[0:250] + "..\n#IshwarTweeting")
	print (str(i) + " times quote tweeted")
	i = i + 1
	time.sleep(time_interval)
