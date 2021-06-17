import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data(urls):
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
        print(price)
        veg = vegitable_name.get_text()


    return shop_name,veg,price

# BIGBASKET LINKS
urls = [
    "https://www.jiomart.com/p/groceries/amaranthus-1-bunch/590003517",
    "https://www.jiomart.com/p/groceries/bhendi-okra-per-kg/590003550",
    "https://www.jiomart.com/p/groceries/lentil-sprouts-200-g/590003515",
    "https://www.jiomart.com/p/groceries/tapioca-1-kg/590003516",
    "https://www.jiomart.com/p/groceries/yam-whole-per-pc/590049201",
    "https://www.jiomart.com/p/groceries/lemon-100-g/590004153",
    "https://www.bigbasket.com/pd/40022638/fresho-tomato-local-organically-grown-500-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop",
    "https://www.bigbasket.com/pd/10000144/fresho-ladies-finger-500-g/",
    "https://www.bigbasket.com/pd/10000148/fresho-onion-1-kg/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop",
    "https://www.bigbasket.com/pd/10000159/fresho-potato-1-kg/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop",
    "https://www.bigbasket.com/pd/40050086/fresho-ash-gourd-cut-250-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop",
    "https://www.bigbasket.com/pd/40050087/fresho-pumpkin-green-cut-500-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop",
    "https://www.bigbasket.com/pd/40201308/fresho-yam-1-pc/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop",
    "https://www.bigbasket.com/pd/10000185/fresho-snake-gourd-500-g/?nc=as&q=Snakeguar",
    "https://www.bigbasket.com/pd/10000127/fresho-lemon-250-g/",
    "https://www.bigbasket.com/pd/10000197/fresho-tapioca-500-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop",
    "https://www.klfresh.com/products/product-detail/tomato/1154",
    "https://www.klfresh.com/products/product-detail/ladies-finger/1153",
    "https://www.klfresh.com/products/product-detail/onionulli/1135",
    "https://www.klfresh.com/products/product-detail/potato-smallurulakizhangu/1151",
    "https://www.klfresh.com/products/product-detail/ash-gourd-kumbalanga/1149",
    "https://www.klfresh.com/products/product-detail/pumpkin-greenmathenga/1125",
    "https://www.klfresh.com/products/product-detail/yam-elephant-foot-chena/1111",
    "https://www.klfresh.com/products/product-detail/snake-gourd-padavalam/1144",
    "https://www.klfresh.com/products/product-detail/lemon/1127",
    "https://www.klfresh.com/products/product-detail/tapiocakolli/1147",
        ]


shop = []
veg = []
rs = []
for url in urls:
    shop_name,vegitable_name,price = get_data(urls=url)
    shop.append(shop_name)
    veg.append(vegitable_name)
    rs.append(price)

datas = pd.DataFrame({
    'Shop-Name': shop,
    'Vegitable-Name': veg,
    'Price': rs,
})

print(datas)
datas.to_csv("hey.csv")



