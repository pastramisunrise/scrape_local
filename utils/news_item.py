import pymongo

class Item():

    def __init__(self, item):
        self.title = item[0]
        self.description = item[1]
        self.link = item[2]
        self.date = item[3]
        self.run_date = item[4]

    def check_item(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["scrape_local"]
        mycol = mydb["search_results"]
        myquery = {"title" : self.title}
        mydoc = mycol.find(myquery).count()
        if mydoc > 0:
            return False
        else:
            check = self.check_story()
            print(check)

    # If not already in DB, sentiment analysis to see if the story matches the criteria
    def check_story(self):
        biz_dict = {
            "opening" : 0,
            "new" : 0,
            "sale" : 0,
            "closing" : 0,
            "restaurant" : 0,
            "store" : 0,
            "club" : 0,
            "shop" : 0,
            "loans" : 0,
            "money" : 0,
            "free" : 0,
            "liquidation": 0,
            "auction" : 0
        }

        title = self.title.lower().split()
        desc = self.description.lower().split()

        print("{}\n".format(title))
        print("{}\n".format(desc))

        for word in title:
            for b in biz_dict:
                if b in word:
                    biz_dict[b] += 1

        for word in desc:
            for b in biz_dict:
                if b in word:
                    biz_dict[b] += 1

        return biz_dict