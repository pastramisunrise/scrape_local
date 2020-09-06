import threading
from utils.openpa_search import Search

if __name__ == "__main__":
    bl_url = "https://phl.carto.com/api/v2/sql?q=SELECT * FROM business_licenses WHERE mostrecentissuedate > now() - interval '1 month' AND initialissuedate > now() - interval '1 year'"
    cal_url = "https://phl.carto.com/api/v2/sql?q=SELECT * FROM com_act_licenses WHERE issuedate > now() - interval '1 month'"
    search_bl = Search("business_licenses", bl_url)
    search_cal = Search("commercial_activity_license", cal_url)
    t1 = threading.Thread(target=search_bl.query_tables())
    t2 = threading.Thread(target=search_cal.query_tables())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Search complete")
    pass