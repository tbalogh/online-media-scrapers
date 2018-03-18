import os
import scrapy

from .ps_archive_url_provider import PsArchiveUrlProvider
from ..article_storage import ArticleStorage

from executor_logger.logger import Logger

class PsSpider(scrapy.Spider):
    name = "ps"
    
    def __init__(self, *args, **kwargs):
        super(PsSpider, self).__init__(*args, **kwargs)
        self.validate_args()
        self.output_root = self.output_root.rstrip('/')
        self.storage = ArticleStorage(self.output_root)
        self.log = Logger(self.output_root + '/scraper.log' )
        self.article_url_xpath = '//div[@class="story-contain left relative infinite-post"]//a[@rel="bookmark"]/@href'
        self.archiveUrlProvider = PsArchiveUrlProvider()
        self.start_page = 1
        self.to_page = int(self.pages)

    def start_requests(self):
        for url in self.archiveUrlProvider.urls(self.start_page, self.to_page):
            yield scrapy.Request(url=url, callback=self.crawl_articles)

    def crawl_articles(self, response):
        article_urls = response.xpath(self.article_url_xpath).extract()
        for url in article_urls:
            yield scrapy.Request(url=url, callback=self.process_article)

    def process_article(self, response):
        try:
            self.storage.save(response.body.decode('utf-8', 'ignore'), response.url)
        except:
            self.log.error("Error parsing and save: " + response.url + "\t" + str(sys.exc_info()[0]))

    def validate_args(self):
        if not hasattr(self, 'output_root'):
            raise ValueError("output_root argument is missing. You should pass it like 'scrapy crawl index -a output_root=<path>' ")

        if not hasattr(self, 'pages'):
            raise ValueError("pages argument is missing. You should pass it like 'scrapy crawl index -a pages=<number>' \n 1 page means ~10-30 article")