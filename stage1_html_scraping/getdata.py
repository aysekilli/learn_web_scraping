import requests
from bs4 import BeautifulSoup
import csv 
import time

url = "https://books.toscrape.com"
response = requests.get(url)
response.encoding = "utf-8" #bazı sitelerde encoding sorunları olabilir, bu yüzden utf-8 olarak ayarlıyoruz ki bouzk karakterleri düzgün görebilelim.

print(response.text)        #genelde utf-8

soup = BeautifulSoup(response.text, "html.parser") 
#html parse eder

#tek element bulmak ixin:
booktitle = soup.find("h1")
print(booktitle.text)

#birden fazla element bulmak için:
books = soup.find_all("article", class_="product_pod")

#veri cekmek icin allbooks'un icine giriyoruz ve h3 tag'inin icindeki a tag'inin title attribute'unu cekiyoruz
for book in books:

    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.strip() #strip() ile başındaki ve sonundaki boşlukları temizliyoruz
    stock = book.find("p", class_="instock").text.strip() 
    stars = book.find("p", class_="star-rating")["class"][1] #class attribute'u bir liste döndürür, ilk eleman "star-rating" olduğu için ikinci elemanı alıyoruz
    print(f"Title: {title:<50}, Price: {price:>8}, Stock: {stock}, Stars: {stars:<6}")

