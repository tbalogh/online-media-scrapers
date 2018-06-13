FROM python:3.6
COPY ./online-media-scrapers /opt/online-media-scrapers
WORKDIR /opt/online-media-scrapers
#RUN apt-get install software-properties-common python-software-properties && \
#    add-apt-repository ppa:pypa/ppa && \ 
#    apt-get update && \
#    apt-get install pipenv
RUN pip install pipenv
RUN pipenv --three && pipenv install
ENTRYPOINT ["pipenv", "run", "scrapy", "crawl"]
CMD ["scrapy", "crawl"]

