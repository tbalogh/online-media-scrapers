# Introduction

This project contains spiders/scrapers that can crawl/scrape articles of hungarian online news portals such as http://index.hu or http://origo.hu. The spiders discovers and download articles as followings:
1. Spiders configured with start_date-end_date pair (or with a custom number) and with an output_root directory
2. Based on the parameters the spiders discovers the archive urls, such as: http://index.hu/belfold/2018/01/01
3. Spiders discover the article urls on the archive urls, such as http://index.hu/belfold/2018/01/01/<article_title>
4. The spiders save the html content in the give output_root with a generated name. (file names usually genereted based on the article title.) 


# Install dependencies

Use pipenv installing dependencies

```
pipenv --three

pipenv shell

pipenv install

```

# Usage

The index/origo/444 and the ps/nynyny scrapers has the same usage.

```
scrapy crawl <[index|origo|nnn]> -a output_root=<output_path> -a start_date=<YYYY/MM/DD> end_date=<YYYY/MM/DD>

scrapy crawl <[ps|nynyny]> -a output_root=<output_path> -a pages=<number>
```
