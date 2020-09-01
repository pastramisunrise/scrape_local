import datetime
from dateutil.relativedelta import relativedelta
import requests
import re
from bs4 import BeautifulSoup
from GoogleNews import GoogleNews
from utils.news_item import Item

class Search():

    # 1. Get local news items

    # Google News Search
    def google_api(self):
        now = datetime.datetime.now()
        googlenews = GoogleNews()
        googlenews.setlang("en")
        googlenews.setperiod("30d")
        googlenews.setencode("utf-8")
        googlenews.search("Philadelphia AND ((Store OR Business) AND (Opening OR New))")
        result = googlenews.result()
        for r in result:
            item = Item([r["title"],r["desc"],r["link"],r["date"],now])
            item.check_item()

    # Patch.com web scraping
    def patch_scrap(self):
        now = datetime.datetime.now()
        page = requests.get("https://patch.com/pennsylvania/philadelphia/business")
        soup = BeautifulSoup(page.text, "html.parser")
        regex = re.compile(".*styles_Card__Content__.*")
        cards = soup.find_all("div", {"class":regex})
        now = datetime.datetime.now()
        start_date = now - relativedelta(days = 30)
        for c in cards:
            date = datetime.datetime.strptime(c.find("time")["datetime"], "%Y-%m-%dT%H:%M:%SZ")
            if date > start_date:
                title = c.find("a")
                link = title["href"]
                title = title.text
                desc = c.find("p")
                desc= desc.text
                item = Item([title,desc,link,date,now])
                item.check_item()

    # Future Iterations
    # 1. Check Craigslist for computer gigs
    # 2. Check Craigslist all jobs at newly opening businesses
    # 3. Check social media for mentions of new businesses
        
    # 4. Add matching items to DB

    # 5. Find lead info