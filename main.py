import os
import time

import tweepy
from tweepy import Response, Tweet
from loguru import logger
from typing import List


class TwitterBot:

    def __init__(self, api: str, api_secret: str, token: str, token_secrect: str, bearer_token: str):
        self.client = tweepy.Client(consumer_key=api,
                                    consumer_secret=api_secret,
                                    access_token=token,
                                    access_token_secret=token_secrect,
                                    bearer_token=bearer_token,
                                    wait_on_rate_limit=True)

    def __on_mention(self, tweet, prefix):
        """
        Perform some action upon receiving a mention.
        """
        # self.post_tweet(text)
        raise NotImplementedError("You need to implement this to reply to/fav mentions (or pass if you don't want to)!")

    def __check_mentions(self):
        """
        Checks mentions and loads most recent tweets into the mention queue
        """

        ...

    def run(self):
        while True:
            try:
                # Check mention
                self.__check_mentions()

                # Retweet
                self.client.retweet('user_id')

            except Exception as error:
                logger.error(error)
                time.sleep(60)


@logger.catch
def run():
    twitter_bot = TwitterBot(os.getenv('API_KEY'),
                             os.getenv('API_KEY_SECRET'),
                             os.getenv('ACCESS_TOKEN'),
                             os.getenv('ACCESS_TOKEN_SECRET'),
                             os.getenv('BEARER_TOKEN'))

    query = '-from:BolhaDados -is:retweet ((#BolhaDados) OR (@BolhaDados))'

    resp: Response = twitter_bot.client.search_recent_tweets(query=query, max_results=10)
    print(resp)
    tweets: List[Tweet] = resp.data

    if tweets is not None:
        print(len(tweets))
        for tweet in tweets:
            print('Retwitand id:', tweet.data)
            twitter_bot.client.retweet(tweet.id)
            twitter_bot.client.like(tweet.id)


    # twitter_bot.run()


if __name__ == '__main__':
    run()
