import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from origo_daily_archive_url_provider import OrigoDailyArchiveUrlProvider
import datetime

import unittest

class TestOrigoDailyArchiveUrlProvider(unittest.TestCase):
    dailyArchiveUrlProvider = OrigoDailyArchiveUrlProvider()

    def test_urls(self):
        test_map = {
            datetime.date(2017, 2, 28): 'http://www.origo.hu/hir-archivum/2017/20170228.html',
            datetime.date(2017, 1, 1): 'http://www.origo.hu/hir-archivum/2017/20170101.html',
            datetime.date(2017, 12, 31): 'http://www.origo.hu/hir-archivum/2017/20171231.html'
        }
        for key, value in test_map.items():
            assert self.dailyArchiveUrlProvider.url(key) == value

    def test_provide_origo_urls(self):
        test_map = {
            ('2017/02/26', '2017/03/01'): [
                'http://www.origo.hu/hir-archivum/2017/20170301.html',
                'http://www.origo.hu/hir-archivum/2017/20170228.html',
                'http://www.origo.hu/hir-archivum/2017/20170227.html',
                'http://www.origo.hu/hir-archivum/2017/20170226.html',
            ],
            ('2016/12/30', '2017/01/01'): [
                'http://www.origo.hu/hir-archivum/2017/20170101.html',
                'http://www.origo.hu/hir-archivum/2016/20161231.html',
                'http://www.origo.hu/hir-archivum/2016/20161230.html',
            ],
            ('2017/11/9', '2017/11/11'): [
                'http://www.origo.hu/hir-archivum/2017/20171111.html',
                'http://www.origo.hu/hir-archivum/2017/20171110.html',
                'http://www.origo.hu/hir-archivum/2017/20171109.html',
            ]
        }
        for (start_date, end_date), expected in test_map.items():
                urls = self.dailyArchiveUrlProvider.urls_between(start_date, end_date)
                self.assertEqual(sorted(urls), sorted(expected))
