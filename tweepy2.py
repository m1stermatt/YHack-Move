import json
import tweepy

tweets = {}
tweets["data"] = []


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")
        with open("tweets.json", "w") as outfile:
            print(f"{tweet.user.name}: {tweet.text}")
            tweets["data"].append(f"{tweet.user.name}: {tweet.text}")
            json.dump(tweets, outfile)

    def on_error(self, status):
        print("Error detected")


# Authenticate to Twitter
auth = tweepy.OAuthHandler("riZgo4htVPjbx38pCZJUv3xgH",
                           "TdbK0JCnkxnybKt9GQ3cRW0RBrwOM5PQinfyDWeeoJVnWSqMAa")
auth.set_access_token("751389655841574913-wkQyKB6bowb0yHlVooeMEZK1cH4SvEA",
                      "12FwyrPdYDxwGBiSxhcGtYcZRDzAgBpqmnLPiRZbjNry3")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["JetBlue", "jetblue"], languages=["en"])
