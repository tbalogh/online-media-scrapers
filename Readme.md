# Introduction

This project contains scrapers that can scrape articles of hungarian online news portals such as http://index.hu or http://origo.hu. The scrapers discovers and download articles as followings:
1. Scrapers configured with start_date-end_date pair (or with a custom number) and with an output_root directory
2. Based on the parameters the scrapers discovers the archive urls, such as: http://index.hu/belfold/2018/01/01
3. Scrapers discover the article urls on the archive urls, such as http://index.hu/belfold/2018/01/01/<article_title>
4. The scrapers save the html content in the give output_root with a generated name. (file names usually genereted based on the article title.) 

http://pestisracok.hu and http://888.hu can not be scraped with between a start_date and end_date however you can pass a number (pages) parameter to it. They organize their content as an infinite list of articles, and when you scroll down it will load content (new "pages") coninuously. So you can specify with a number parameter how many "pages" you want to crawl.

# Dependencies

Docker

# Usage

## Without docker

You can use it without docker. [Read using directly here](online-media-scrapers/Readme.md)

## Already built Docker ismage
[Find the image and description here](https://hub.docker.com/r/tbalogh/online-media-scrapers/)

## Build the image
```
docker build -t <tag> . 
```

example:
```
docker build -t scrapers . 
```
## Run the image

### For scraping index, origo, 444:

```bash
docker run -i -v<path/to/save/result/on/your/local/machine/>:/opt/articles <tag> <[index|origo|nnn]> -a output_root=/opt/articles -a start_date=<YYYY/MM/DD> -a end_date=<YYYY/MM/DD>
```

Example:

```bash
docker run -i -v"$(pwd)/index":/opt/articles scrapers index -a output_root=/opt/articles -a start_date=2018/03/01 -a end_date=2018/03/02
```

### For scraping pestisracok, 888:

```bash
docker run -i -v<path/to/save/result/on/your/local/machine/>:/opt/articles <tag> <[ps|nynyny]> -a output_root=/opt/articles -a start_page=<number> -a end_page<number>
```

example:
```bash
docker run -i -v"$(pwd)/ps":/opt/articles scrapers ps -a output_root=/opt/articles -a start_page=1 -a end_page=2
```