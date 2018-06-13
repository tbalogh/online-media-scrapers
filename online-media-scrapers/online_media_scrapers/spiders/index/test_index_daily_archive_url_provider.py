import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import unittest

from index_daily_archive_url_provider import IndexDailyArchiveUrlProvider
import datetime

class TestIndexDailyArchiveUrlProvider(unittest.TestCase):
    dailyArchiveUrlProvider = IndexDailyArchiveUrlProvider()

    def test_provide_index_urls_between_dates(self):
        test_map = {
            ("2017/02/28", "2017/03/01"): [
                'http://index.hu/belfold/2017/02/28', 'http://index.hu/kulfold/2017/02/28',
                 'http://index.hu/gazdasag/2017/02/28',
                'http://index.hu/belfold/2017/03/01', 'http://index.hu/kulfold/2017/03/01',
                 'http://index.hu/gazdasag/2017/03/01'
            ],
            ("2016/12/31", "2017/01/01"): [
                'http://index.hu/belfold/2016/12/31', 'http://index.hu/kulfold/2016/12/31',
                 'http://index.hu/gazdasag/2016/12/31',
                'http://index.hu/belfold/2017/01/01', 'http://index.hu/kulfold/2017/01/01',
                 'http://index.hu/gazdasag/2017/01/01',
            ],
            ("2016/12/01", "2016/12/01"): ['http://index.hu/belfold/2016/12/01',
                                              'http://index.hu/kulfold/2016/12/01',
                                              'http://index.hu/gazdasag/2016/12/01']
        }
        for (start_date, end_date), expected_urls in test_map.items():
            actual_urls = self.dailyArchiveUrlProvider.urls_between(start_date, end_date)
        self.assertEqual(sorted(actual_urls), sorted(expected_urls))
