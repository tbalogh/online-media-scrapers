import os
from urllib.parse import urlparse

from file_utils.file_utils import save


class ArticleStorage:
    def __init__(self, path):
        if path:
            self.base_path = path.rstrip('/')
        else:
            self.base_path = os.path.dirname(os.path.abspath(__file__))

    def save(self, html_page_text, url):
        path = self.base_path + '/' + self.name_from(url)
        save(html_page_text, path)

    @staticmethod
    def name_from(url):
        return urlparse(url).path.rstrip('/').rstrip('.html').lstrip('/') + '.html'
