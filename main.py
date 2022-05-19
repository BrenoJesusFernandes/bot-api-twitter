import tweepy
from loguru import logger


@logger.catch
def run():

    raise Exception('xablau!')

    while True:
        ...


if __name__ == '__main__':
    logger.add('log/error.log')
    run()
