class PsArchiveUrlProvider:
    base_url = "http://pestisracok.hu"

    def url(self, index):
        if index is 0:
            return self.base_url
        else:
            return self.base_url + "/page/" + str(index)

    def urls(self, start_index, end_index):
        if end_index - start_index <= 0:
            return []
        for i in range(start_index, end_index+1):
            yield self.url(i)
