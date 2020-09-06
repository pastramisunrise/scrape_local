import json
import requests
from utils.business import Business
from utils.search import Search

class OPA_Search(Search):
    def query_tables(self):
        print("{} search starting...".format(self.name))
        r = requests.get(self.url)
        data = json.loads(r.text)
        for row in data["rows"]:
            business = Business(row, self.name)
            search_result = business.find_bus()
            if search_result:
                print("{} record found on table, skipping".format(self.name))
            else:
                print("{} record not found on table, adding record".format(self.name))
                add_result = business.add_record()
                print("Saved with record ID: {}".format(add_result))