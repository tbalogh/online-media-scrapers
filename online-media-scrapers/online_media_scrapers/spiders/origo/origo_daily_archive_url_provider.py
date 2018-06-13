import datetime

def as_two_digit_string(num):
    num_str = str(num)
    if len(num_str) == 1: num_str = '0' + num_str
    return num_str


def as_string(date, delimiter):
    year = date.year
    month = as_two_digit_string(date.month)
    day = as_two_digit_string(date.day)

    return str(year) + delimiter + str(month) + delimiter + str(day)


class OrigoDailyArchiveUrlProvider:
    def __init__(self):
        self.base_url = 'http://www.origo.hu/hir-archivum'

    def url(self, date):
        return self.base_url + '/' + str(date.year) + '/' + as_string(date, '') + '.html'

    def urls_between(self, start_date_str, end_date_str):
        SEP = '/'
        start = datetime.datetime.strptime(start_date_str, '%Y' + SEP + '%m' + SEP + '%d')
        end = datetime.datetime.strptime(end_date_str, '%Y' + SEP + '%m' + SEP + '%d')
        step = datetime.timedelta(days=1)
        urls = []
        while start <= end:
            urls.append(self.url(start.date()))
            start += step

        return urls
