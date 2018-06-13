import sys, os, datetime
import scrapy

from ..article_storage import ArticleStorage
from ..index.index_daily_archive_url_provider import IndexDailyArchiveUrlProvider

from executor_logger.logger import Logger


class IndexSpider(scrapy.Spider):
    name = "index"

    def __init__(self, *args, **kwargs):
        super(IndexSpider, self).__init__(*args, **kwargs)
        self.validate_args()
        self.output_root = self.output_root.rstrip('/')
        self.storage = ArticleStorage(self.output_root)
        datetime_str = datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
        self.log = Logger(os.getcwd() + '/index_' + datetime_str  + 'spider.log')
        self.article_url_xpath = '//li/h1/a[@class="cim"]/@href'
        self.archive_url_provider = IndexDailyArchiveUrlProvider()

    def start_requests(self):
        for url in self.archive_url_provider.urls_between(self.start_date, self.end_date):
            yield scrapy.Request(url=url, callback=self.crawl_articles)

    def crawl_articles(self, response):
        for article_url in response.xpath(self.article_url_xpath).extract():
            yield scrapy.Request(url=article_url, callback=self.parse)

    def parse(self, response):
        try:
            self.storage.save(response.body.decode('utf-8', 'ignore'), response.url)
            self.log.info("URL SAVED", response.url)
        except  :
            self.log.error("Error parsing and save: " + response.url + "\t" + str(sys.exc_info()[0]))

    def validate_args(self):
        if not hasattr(self, 'output_root'):
            raise ValueError(
                "output_root argument is missing. You should pass it like 'scrapy crawl index -a output_root=<path>' ")
        if not hasattr(self, 'start_date'):
            raise ValueError(
                "start_date argument is missing. You should pass it like 'scrapy crawl index -a start_date=YYYY/MM/DD' ")
        if not hasattr(self, 'end_date'):
            raise ValueError(
                "end_date argument is missing. You should pass it like 'scrapy crawl index -a end_date=YYYY/MM/DD' ")
