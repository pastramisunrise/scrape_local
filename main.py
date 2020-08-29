from GoogleNews import GoogleNews

# 1. Get local news items

# Google News Search
search_keys = [
    "Philadelphia AND ((Store OR Business) AND (Opening OR New))"
]

for s in search_keys:
    googlenews = GoogleNews()
    googlenews.setlang("en")
    googlenews.setperiod("30d")
    googlenews.setencode("utf-8")
    googlenews.search(s)
    print(googlenews.gettext())

# Patch.com web scraping

# 2. Check if items are already in the local database

# 3. If not already in DB, sentiment analysis to see if the story matches the criteria

# 4. Add matching items to DB