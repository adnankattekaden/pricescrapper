import requests
from bs4 import BeautifulSoup
import pandas as pd


def bigbasket(url):
    webiste_name = url.split(".")
    shop_name = webiste_name[1]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    vegitable_name = soup.find_all("h1", class_="GrE04")
    price = soup.find_all("td", class_="IyLvo")

    print("Shop-Name:-", shop_name)
    print("Vegitable:-", vegitable_name[0].get_text())
    print("Price:-", price[0].get_text())

def jiomart(url):
    webiste_name = url.split(".")
    shop_name = webiste_name[1]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    vegitable_name = soup.find_all("div", class_="title-section")
    price = soup.find_all("span", class_="final-price")

    print("Shop-Name:-", shop_name)
    print("Vegitable:-", vegitable_name[0].get_text())
    print("Price:-", price[0].get_text())

def klfresh(url):
    webiste_name = url.split(".")
    shop_name = webiste_name[1]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    vegitable_name = soup.find("div", class_="mr-2")
    price = soup.find_all("span", class_="t3-mainPrice mr-5")

    print("Shop-Name:-", shop_name)
    print("Vegitable:-", vegitable_name.get_text())
    print("Price:-", price[0].get_text())

# BIGBASKET LINKS
bigbasket(url="https://www.bigbasket.com/pd/40022638/fresho-tomato-local-organically-grown-500-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop")
bigbasket(url="https://www.bigbasket.com/pd/10000144/fresho-ladies-finger-500-g/")
bigbasket(url="https://www.bigbasket.com/pd/10000148/fresho-onion-1-kg/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop")
bigbasket(url="https://www.bigbasket.com/pd/10000159/fresho-potato-1-kg/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop")
bigbasket(url="https://www.bigbasket.com/pd/40050086/fresho-ash-gourd-cut-250-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop")
bigbasket(url="https://www.bigbasket.com/pd/40050087/fresho-pumpkin-green-cut-500-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop")
bigbasket(url="https://www.bigbasket.com/pd/40201308/fresho-yam-1-pc/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop")
bigbasket(url="https://www.bigbasket.com/pd/10000185/fresho-snake-gourd-500-g/?nc=as&q=Snakeguar")
bigbasket(url="https://www.bigbasket.com/pd/10000127/fresho-lemon-250-g/")
bigbasket(url="https://www.bigbasket.com/pd/10000197/fresho-tapioca-500-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop")

#jiomart links
jiomart(url="https://www.jiomart.com/p/groceries/amaranthus-1-bunch/590003517")
jiomart(url="https://www.jiomart.com/p/groceries/bhendi-okra-per-kg/590003550")
jiomart(url="https://www.jiomart.com/p/groceries/lentil-sprouts-200-g/590003515")
jiomart(url="https://www.jiomart.com/p/groceries/tapioca-1-kg/590003516")
jiomart(url="https://www.jiomart.com/p/groceries/yam-whole-per-pc/590049201")
jiomart(url="https://www.jiomart.com/p/groceries/lemon-100-g/590004153")

#klfresh links
klfresh(url="https://www.klfresh.com/products/product-detail/tomato/1154")
klfresh(url="https://www.klfresh.com/products/product-detail/ladies-finger/1153")
klfresh(url="https://www.klfresh.com/products/product-detail/onionulli/1135")
klfresh(url="https://www.klfresh.com/products/product-detail/potato-smallurulakizhangu/1151")
klfresh(url="https://www.klfresh.com/products/product-detail/ash-gourd-kumbalanga/1149")
klfresh(url="https://www.klfresh.com/products/product-detail/pumpkin-greenmathenga/1125")
klfresh(url="https://www.klfresh.com/products/product-detail/yam-elephant-foot-chena/1111")
klfresh(url="https://www.klfresh.com/products/product-detail/snake-gourd-padavalam/1144")
klfresh(url="https://www.klfresh.com/products/product-detail/lemon/1127")
klfresh(url="https://www.klfresh.com/products/product-detail/tapiocakolli/1147")