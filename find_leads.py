import threading
from utils.openpa_search import OPA_Search

if __name__ == "__main__":
    bl_url = "https://phl.carto.com/api/v2/sql?q=SELECT * FROM business_licenses WHERE mostrecentissuedate > now() - interval '1 month' AND initialissuedate > now() - interval '1 year'"
    search_bl = OPA_Search("business_licenses", bl_url)
    search_bl.query_tables()
    print("Search complete")
    pass