import requests
from bs4 import BeautifulSoup
from utils.business import Business
from utils.search import Search

if __name__ == "__main__":
    bl = Business({}, "business_licenses")
    all_biz = bl.get_all()
    for x in all_biz:
        print(x)
    # search = Search("", sample["business_name"])
    # search_result = search.search_url()
    # if search_result.status_code == 200:
    #     soup = BeautifulSoup(search_result.text, "html.parser")
    #     link_list = []
    #     for l in soup.find_all("div", class_="r"):
    #         a = l.find_all("a")
    #         if a:
    #             link = a[0]["href"]
    #             title = l.find("h3").text
    #             item = {
    #                 "title": title,
    #                 "link": link
    #             }
    #             link_list.append(item)
    # print(link_list)
    pass