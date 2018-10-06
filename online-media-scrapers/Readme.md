# Introduction

This project contains scrapers that can scrape articles of hungarian online news portals such as http://index.hu or http://origo.hu. The spiders discovers and download articles as followings:
1. Spiders configured with parameters:
* start_date-end_date pair OR with a custom number
* output_root directory
2. Based on the parameters the spiders discovers the archive urls, such as: http://index.hu/belfold/2018/01/01
3. Spiders discover the article urls on the archive urls, such as http://index.hu/belfold/2018/01/01/<article_title>
4. The spiders save the html content in the given output_root with a generated name. (file names usually genereted based on the article title.)

http://pestisracok.hu and http://888.hu can not be scraped with between a start_date and end_date however you can pass a number (pages) parameter to it. They organize their content as an infinite list of articles, and when you scroll down it will load content (new "pages") coninuously. So you can specify with a number parameter how many "pages" you want to crawl.


# Install dependencies

Use pipenv with python 3.6 (python 3.7 does not work with scrapy) installing dependencies

```

pipenv shell

pipenv install

```

# Usage

Hint: -a 

## index, origo and 444:

usage:

```bash
scrapy crawl <[index|origo|nnn]> -a output_root=<output_path> -a start_date=<YYYY/MM/DD> -a end_date=<YYYY/MM/DD>
```

example:
```bash
scrapy crawl index -a output_root=./output/index -a start_date=2018/01/01 -a end_date=2018/01/07
```

## 888, pestisracok:

usage:

```bash
scrapy crawl <[ps|nynyny]> -a output_root=<output_path> -a pages=<number>
```

example:

```bash
scrapy crawl ps -a output_root=./output/ps -a pages=5
```

# Tips

## Missing -a parameter flag

If you see the following error: `scrapy crawl [options] <spider>` than you should check that all parameters (eg.: end_date, output_root ...) has the -a flag before the parameter.