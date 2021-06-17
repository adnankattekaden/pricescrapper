import requests
from bs4 import BeautifulSoup

#
# url = "https://www.bigbasket.com/pd/40022638/fresho-tomato-local-organically-grown-500-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop"
#
# page = requests.get(url)
#
# soup = BeautifulSoup(page.content, "html.parser")
#
# webiste_name = url.split(".")
# vegitable_name = soup.find_all("h1", class_="GrE04")
# price = soup.find_all("td",class_="IyLvo")
#
# print("Shop-Name:-",webiste_name[1])
# print("Vegitable:-",vegitable_name[0].get_text())
# print("Price:-",price[0].get_text())


class ScrapeVegitableDetails():
    def get_data(self,url):
        webiste_name = url.split(".")
        shop_name = webiste_name[1]

        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        if shop_name == "bigbasket":
            vegitable_name = soup.find_all("h1", class_="GrE04")
            price = soup.find_all("td", class_="IyLvo")
        elif shop_name == "jiomart":
            vegitable_name = soup.find_all("div", class_="title-section")
            price = soup.find_all("span", class_="final-price")
        elif shop_name == "klfresh":
            vegitable_name = soup.find("div", class_="mr-2")
            price = soup.find_all("span", class_="t3-mainPrice mr-5")

        print('\n')
        print("Shop-Name:-", shop_name)
        print("Vegitable:-", vegitable_name[0].get_text())
        print("Price:-", price[0].get_text())



bigbasket = ScrapeVegitableDetails()
bigbasket.get_data(url="https://www.bigbasket.com/pd/40022638/fresho-tomato-local-organically-grown-500-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop")
bigbasket.get_data(url="https://www.jiomart.com/p/groceries/amaranthus-1-bunch/590003517")
# bigbasket.get_data(url="https://www.klfresh.com/products/product-detail/onion-tomato-potato-1-kg-each-combo/1301")
