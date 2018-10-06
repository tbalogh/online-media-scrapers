import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from lxml import html

def dailyArchiveResponse():
    with open("./daily_archive_sample.html", 'r') as f:
        return html.fromstring(f.read())


class TestNnnScraper():
    def test(self):
        article_url_xpath = '//article/h3/a/@href'
        dummyResponse = dailyArchiveResponse()
        for url in dummyResponse.xpath(article_url_xpath):
            print(url)
        assert 1 == 2

