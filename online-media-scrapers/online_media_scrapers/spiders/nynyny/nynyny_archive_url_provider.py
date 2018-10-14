class NyNyNyArchiveUrlProvider:
    base_url = "https://888.hu/megtobbetszeretnek/?h="

    def url(self, index):
        return self.base_url + str(self.calculate_h(index))

    def urls(self, start_index, end_index):
        if end_index - start_index <= 0:
            return []
        else:
            for i in range(start_index, end_index + 1):
                yield self.url(i)

    def should_terminate(self, index):
        # 888 is tricky. it uses an "h" query param if we click on "Load more" button, but it only goes around h=26000
        return self.calculate_h(index) > 26100

    def calculate_h(self, index):
        return 36 + index * 36
