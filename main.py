import datetime
from dateutil.relativedelta import relativedelta
import requests
import re
from bs4 import BeautifulSoup
from GoogleNews import GoogleNews

# 1. Get local news items

# Google News Search
def google_api():
    googlenews = GoogleNews()
    googlenews.setlang("en")
    googlenews.setperiod("30d")
    googlenews.setencode("utf-8")
    googlenews.search("Philadelphia AND ((Store OR Business) AND (Opening OR New))")
    print(googlenews.gettext())

# Patch.com web scraping
def patch_scrap():
    page = requests.get("https://patch.com/pennsylvania/philadelphia/business")
    soup = BeautifulSoup(page.text, "html.parser")
    regex = re.compile(".*styles_Card__Content__.*")
    cards = soup.find_all("div", {"class":regex})
    now = datetime.datetime.now()
    print("Current Datetime: {}".format(now))
    start_date = now - relativedelta(days = 30)
    print("Start Datetime: {}".format(start_date))
    for c in cards:
        date = datetime.datetime.strptime(c.find("time")["datetime"], "%Y-%m-%dT%H:%M:%SZ")
        if date > start_date:
        # Get title
        title = c.find("a")
        # link = title["href"]
        # title = title.text
        # Get description
        desc = c.find("p")
        # print(desc.text)

# 2. Check if items are already in the local database
def check_item(item):
    # Connect to DB
    # Create DB
    # Create table
    # Search table
    # Close connection
    # Return result

# 3. If not already in DB, sentiment analysis to see if the story matches the criteria

# 4. Add matching items to DB

# 5. Find lead info