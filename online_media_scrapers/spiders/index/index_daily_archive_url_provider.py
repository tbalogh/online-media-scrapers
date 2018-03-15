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


class IndexDailyArchiveUrlProvider:
    def __init__(self):
        self.base_url = "http://index.hu"
        self.categories = ['belfold', 'kulfold', 'gazdasag']

    def urls_for_date(self, date):
        SEP = '/'
        urls = []
        for category in self.categories:
            url = self.base_url + SEP + category + SEP + as_string(date, SEP)
            urls.append(url)
        return urls

    def urls_between(self, start_date_str, end_date_str):
        SEP = '/'
        start = datetime.datetime.strptime(start_date_str, '%Y' + SEP + '%m' + SEP + '%d')
        end = datetime.datetime.strptime(end_date_str, '%Y' + SEP + '%m' + SEP + '%d')
        step = datetime.timedelta(days=1)
        urls = []
        while start <= end:
            urls.extend(self.urls_for_date(start.date()))
            start += step

        return urls
