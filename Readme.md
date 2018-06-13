# Introduction

This project contains spiders/scrapers that can crawl/scrape articles of hungarian online news portals such as http://index.hu or http://origo.hu. The spiders discovers and download articles as followings:
1. Spiders configured with start_date-end_date pair (or with a custom number) and with an output_root directory
2. Based on the parameters the spiders discovers the archive urls, such as: http://index.hu/belfold/2018/01/01
3. Spiders discover the article urls on the archive urls, such as http://index.hu/belfold/2018/01/01/<article_title>
4. The spiders save the html content in the give output_root with a generated name. (file names usually genereted based on the article title.) 


# Dependencies

Docker

# Usage

## Directly

You can use it without docker. [Read using directly here](online-media-scrapers/Readme.md)

## Already built Docker image
[Find the image and description here](https://hub.docker.com/r/tbalogh/online-media-scrapers/)

## Build the image
```
docker build -t <tag> . 
```

## Run the image
```
docker run -i -v<path_to_save_articles_on_your_machine>:/opt/articles scrapers <[index|origo|nnn]> -a output_root=/opt/articles -a start_date=<YYYY/MM/DD> -a end_date=<YYYY/MM/DD>
```
