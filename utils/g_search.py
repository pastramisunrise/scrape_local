import requests
from utils.search import Search

class G_Search(Search):

    def g_search(self):
        return requests.get("https://www.google.com/search?q={}".format(self.url.replace(" ", "+")))