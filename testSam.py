import tweepy

key = "ACCESS TOKEN HERE"
secret = "ACCESS TOKEN SECRET HERE"
auth = tweepy.OAuthHandler("CONSUMER KEY HERE", "ACCESS TOKEN SECRET HERE")
auth.set_access_token(key, secret)
api = tweepy.API(auth)
tweet = input(" ")
api.update_status(status=(tweet))
print("Done")