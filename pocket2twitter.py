from random import randint, shuffle

import argparse
from datetime import datetime, timedelta
from dateutil.parser import parse
import config
from pocket import Pocket
import pytz
import time
import twitter


ELAPSED_HOURS_DEFAULT = 24
POCKET_ARTICLE_TAG_DEFAULT = 'twitter'

TWITTER_MAX_LENGTH = 280
TWITTER_URL_SHORTENED = 26

pocketAPI = Pocket(
    consumer_key=config.POCKET_CONSUMER_KEY,
    access_token=config.POCKET_ACCESS_TOKEN,
)

twitterAPI = twitter.Twitter(
	auth=twitter.OAuth(
		config.TWITTER_ACCESS_TOKEN_KEY,
		config.TWITTER_ACCESS_TOKEN_SECRET,
		config.TWITTER_CONSUMER_KEY,
		config.TWITTER_CONSUMER_SECRET,
	),
)


def main(args):
    if args.random_delay:
        random_delay(args.random_delay)

    articles = pocketAPI.retrieve(tag=args.article_tag)['list']

    user_timeline = twitterAPI.statuses.user_timeline(count=1)

    if not user_timeline:
        print('Empty Twitter timeline, tweeting anyway!')
    else:
        last_tweet_created = parse(user_timeline[0]['created_at'])
        elapsed_in_hours = pytz.utc.localize(datetime.now()) - last_tweet_created

        if elapsed_in_hours < timedelta(hours=args.elapsed_hours):
            print('No need to tweet now.')
            exit(0)

    all_articles = list(articles.values())

    shuffle(all_articles)

    for details in all_articles:
        if details['status'] != '0' or details['is_article'] != '1':
            continue

        chosen_article = details
        break

    chosen_article_id = int(chosen_article['item_id'])

    tweet = prepare_tweet(chosen_article)

    try:
        twitterAPI.statuses.update(status=tweet)
    except:
        print('Could not tweet status update!')
        exit(1)

    pocketAPI.tags_remove(chosen_article_id, args.article_tag).archive(chosen_article_id).commit()

    print('Tweeted "%s"!' % tweet)

def prepare_tweet(article):
    title = article.get('resolved_title', article['given_title'])
    url = article.get('resolved_url', article['given_url'])

    url_length = len(url)

    if url_length > TWITTER_URL_SHORTENED:
        # It seems to me that the links are shortened to 26 visible characters
        # and then three '.'-s are added? Not totally sure about it tho
        url_length = TWITTER_URL_SHORTENED + 3

    if (len(title) + url_length + 1) > TWITTER_MAX_LENGTH:
        title_maximum_length = TWITTER_MAX_LENGTH - url_length - 4
        title = title[:title_maximum_length] + '...'

    return '%s %s' % (title, url)


def random_delay(max_minutes):
    delay = randint(1, max_minutes - 1)
    print('Waiting %d min' % delay)
    time.sleep(delay * 60)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='pocket2twitter')
    parser.add_argument('--elapsed-hours', type=int, default=ELAPSED_HOURS_DEFAULT)
    parser.add_argument('--article-tag', type=str, default=POCKET_ARTICLE_TAG_DEFAULT)
    parser.add_argument('--random-delay', type=int, default=None)
    args = parser.parse_args()
    main(args)
