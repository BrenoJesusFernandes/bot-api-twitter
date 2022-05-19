import os
import tweepy
from loguru import logger


class TwitterBot:

    def __init__(self, api: str, api_secret: str, token: str, token_secrect: str):
        print(api, api_secret, token, token_secrect)

        self.client = tweepy.Client(consumer_key=api,
                                    consumer_secret=api_secret,
                                    access_token=token,
                                    access_token_secret=token_secrect)

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
        """
        Runs the bot!
        """
        while True:

            # Check mention
            self.__check_mentions()

            # Retweet
            self.client.retweet('user_id')

            ...


@logger.catch
def run():
    twitter_bot = TwitterBot(os.getenv('API_KEY'),
                             os.getenv('API_KEY_SECRET'),
                             os.getenv('ACCESS_TOKEN'),
                             os.getenv('ACCESS_TOKEN_SECRET'))

    resp = twitter_bot.client.create_tweet(text=r'*beep*')
    print(resp)

    # twitter_bot.run()


if __name__ == '__main__':
    logger.add('log/error.log')
    run()
