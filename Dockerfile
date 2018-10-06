FROM python:3.6
COPY ./online-media-scrapers /opt/online-media-scrapers
WORKDIR /opt/online-media-scrapers
#RUN apt-get install software-properties-common python-software-properties && \
#    add-apt-repository ppa:pypa/ppa && \ 
#    apt-get update && \
#    apt-get install pipenv
RUN pip install pipenv

#Workaround for pipenv issue: to manually install scrapy
RUN pipenv --three && pip install scrapy
ENTRYPOINT ["pipenv", "run", "scrapy", "crawl"]
CMD ["scrapy", "crawl"]

