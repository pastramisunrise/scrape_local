import datetime
import requests
import json
from utils.business import Business

class Search():

    def __init__(self):
        self.now = datetime.datetime.now()
        print("Search starting...")

    # Query table
    def query_tables(self):
        bl_url = "https://phl.carto.com/api/v2/sql?q=SELECT * FROM business_licenses WHERE mostrecentissuedate > now() - interval '1 month'"
        cal_url = "https://phl.carto.com/api/v2/sql?q=SELECT * FROM com_act_licenses WHERE issuedate > now() - interval '1 month'"
        tables = {"business_licenses" : bl_url, "commercial_activity_license" : cal_url}

        for tab in tables:
            print("Downloading {} table".format(tab))
            r = requests.get(tables[tab])
            data = json.loads(r.text)
            print("Checking {} table".format(tab))
            for row in data["rows"]:
                business = Business(row, tab)
                search_result = business.find_bus()
                if search_result:
                    add_result = business.add_record()
        print("Search complete")
        
    # Find lead info