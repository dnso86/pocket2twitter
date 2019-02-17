import unittest

import pocket2twitter


class test_prepare_tweet(unittest.TestCase):
    def test_resolved_given(self):
        article_resolved_given = {
            'resolved_title': 'RESOLVED',
            'resolved_url': 'www.github.com',
            'given_title': 'NotResolved',
            'given_url': 'www.github.com/aardvark',
        }

        self.assertEqual(
            pocket2twitter.prepare_tweet(article_resolved_given),
            'RESOLVED www.github.com')


    def test_resolved_missing(self):
        article_resolved_given = {
            'given_title': 'NotResolved',
            'given_url': 'www.github.com/aardvark',
        }

        self.assertEqual(
            pocket2twitter.prepare_tweet(article_resolved_given),
            'NotResolved www.github.com/aardvark')


    def test_very_long_url(self):
        article_very_long_url = {
            'given_title': 'NotResolved',
            'given_url': 'www.github.com/aardvark/cf23df2207d99a74fbe169e3eba035e633b65d94',
        }

        self.assertEqual(
            pocket2twitter.prepare_tweet(article_very_long_url),
            'NotResolved www.github.com/aardvark/cf23df2207d99a74fbe169e3eba035e633b65d94')


    def test_very_long_title(self):
        article_very_long_title = {
            'given_title': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. ',
            'given_url': 'www.github.com/aardvark',
        }

        self.assertEqual(
            pocket2twitter.prepare_tweet(article_very_long_title),
            'Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea... www.github.com/aardvark')

        self.assertTrue(len(pocket2twitter.prepare_tweet(article_very_long_title)) <= pocket2twitter.TWITTER_MAX_LENGTH)


if __name__ == '__main__':
    unittest.main()
