import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import unittest

from nnn_daily_archive_url_provider import NnnDailyArchiveUrlProvider
import datetime


class TestNnnDailyArchiveUrlProvider(unittest.TestCase):
    dailyArchiveUrlProvider = NnnDailyArchiveUrlProvider()

    def test_provide_nnn_url(self):
        test_map = {
            datetime.date(2017, 2, 28): 'https://444.hu/2017/02/28',
            datetime.date(2017, 1, 1): 'https://444.hu/2017/01/01',
            datetime.date(2017, 12, 31): 'https://444.hu/2017/12/31'
        }
        for key, value in test_map.items():
            assert self.dailyArchiveUrlProvider.url(key) == value

    def test_provide_nnn_urls(self):
        test_map = {
            ('2017/02/26', '2017/03/01'): [
                'https://444.hu/2017/03/01',
                'https://444.hu/2017/02/28',
                'https://444.hu/2017/02/27',
                'https://444.hu/2017/02/26',
            ],
            ('2016/12/30', '2017/01/01'): [
                'https://444.hu/2017/01/01',
                'https://444.hu/2016/12/31',
                'https://444.hu/2016/12/30',
            ],
            ('2017/11/9', '2017/11/11'): [
                'https://444.hu/2017/11/11',
                'https://444.hu/2017/11/10',
                'https://444.hu/2017/11/09',
            ]
        }
        for (start_date, end_date), expected in test_map.items():
            urls = self.dailyArchiveUrlProvider.urls_between(start_date, end_date)
            self.assertEqual(sorted(urls), sorted(expected))
