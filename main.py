import requests
from bs4 import BeautifulSoup
import pandas as pd
from links_list import urls

def get_data(url):
    webiste_name = url.split(".")
    shop_name = webiste_name[1]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    if shop_name == "bigbasket":
        vegitable_name = soup.find_all("h1", class_="GrE04")
        final_price = soup.find_all("td", class_="IyLvo")
        price = final_price[0].get_text()
        veg = vegitable_name[0].get_text()

    elif shop_name == "jiomart":
        vegitable_name = soup.find_all("div", class_="title-section")
        price = soup.find_all("span",class_="final-price")

        for i in price:
            old_price = i.text
            price = old_price.split(":")[1]
        veg = vegitable_name[0].get_text()

    elif shop_name == "klfresh":
        vegitable_name = soup.find("div", class_="mr-2")
        final_price = soup.find_all("span", class_="t3-mainPrice mr-5")
        price = final_price[0].get_text()
        price = price.split("/")[0]
        veg = vegitable_name.get_text()

    return shop_name,veg,float(price.split()[-1])

shops_list = []
vegitables_list = []
prices_list = []

for url in urls:
    shop_name,vegitable_name,price = get_data(url)
    shops_list.append(shop_name)
    vegitables_list.append(vegitable_name)
    prices_list.append(price)


datas = pd.DataFrame({
    'Shop-Name': shops_list,
    'Vegitable-Name': vegitables_list,
    'Price': prices_list,
})

print(datas)

datas.to_csv("Fetch-Price.csv")



