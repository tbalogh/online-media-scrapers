import os, sys, datetime
import scrapy

from ..origo.origo_daily_archive_url_provider import OrigoDailyArchiveUrlProvider
from ..article_storage import ArticleStorage
from ..logger import Logger

class OrigoSpider(scrapy.Spider):
    name = "origo"

    def __init__(self, *args, **kwargs):
        super(OrigoSpider, self).__init__(*args, **kwargs)
        self.validate_args()
        self.output_root = self.output_root.rstrip('/')
        self.storage = ArticleStorage(self.output_root)
        datetime_str = datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
        self.log = Logger(os.getcwd() + '/origo' + datetime_str  + '.spider.log')
        self.article_url_xpath = '//div[@class="archive-cikk"]/h3/a/@href'
        self.archive_url_provider = OrigoDailyArchiveUrlProvider()

    def start_requests(self):
        for url in self.archive_url_provider.urls_between(self.start_date, self.end_date):
            yield scrapy.Request(url=url, callback=self.crawl_articles)

    def crawl_articles(self, response):
        for article_url in response.xpath(self.article_url_xpath).extract():
            yield scrapy.Request(url=article_url, callback=self.process_article)

    def process_article(self, response):
        try:
            self.storage.save(response.body.decode('iso-8859-2', 'ignore'), response.url)
            self.log.info("URL PROCESSED", response.url)
        except:
            self.log.error("Error parsing and save: " + response.url + "\t" + str(sys.exc_info()[0]))

    def validate_args(self):
        if not hasattr(self, 'output_root'):
            raise ValueError(
                "output_root argument is missing. You should pass it like 'scrapy crawl <spider_name> -a output_root=<path>' ")
        if not hasattr(self, 'start_date'):
            raise ValueError(
                "start_date argument is missing. You should pass it like 'scrapy crawl <spider_name> -a start_date=YYYY/MM/DD' ")
        if not hasattr(self, 'end_date'):
            raise ValueError(
                "end_date argument is missing. You should pass it like 'scrapy crawl <spider_name> -a end_date=YYYY/MM/DD' ")
