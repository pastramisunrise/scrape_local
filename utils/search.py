import requests

class Search():
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def search_url(self):
        return requests.get("https://www.duckduckgo.com/search?q={}".format(self.url.replace(" ", "+")))