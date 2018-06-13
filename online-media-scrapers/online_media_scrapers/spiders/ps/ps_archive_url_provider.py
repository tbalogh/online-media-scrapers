class PsArchiveUrlProvider:
    base_url = "http://pestisracok.hu"

    def url(self, index):
        if index is 0:
            return self.base_url
        else:
            return self.base_url + "/page/" + str(index)

    def urls(self, start_index, counter):
        if counter is 0:
            return []
        for i in range(start_index, start_index + counter):
            yield self.url(i)
