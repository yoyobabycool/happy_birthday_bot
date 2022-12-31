#happy_bday_bro
import tweepy
import datetime
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
def tweet():
    try:
        mydate = datetime.datetime.now()
        mon = mydate.strftime("%B")
        day = str(mydate.day)
        api.update_status(status = 'Happy Birthday to everyone born on ' + mon + ' ' + day)
        print(mydate)
        print("tweeted")
    except Exception as e:
        print("error occurred")
        print(e)
tweet()
