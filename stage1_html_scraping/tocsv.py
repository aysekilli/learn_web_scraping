import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

all_books = []
page = 1

while True:
    print(f"Downloading page {page}...")

    url = BASE_URL.format(page)
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    
    #bu sayfadaki kitaplari cek
    books = soup.find_all("article", class_="product_pod")
    for book in books:
        name = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        stars = book.find("p", class_="star-rating")["class"][1] #class attribute'u bir liste döndürür, ilk eleman "star-rating" olduğu için ikinci elemanı alıyoruz
        stock = book.find("p", class_="instock").text.strip()

        all_books.append({
            "name": name,
            "price": price,
            "stars": stars,
            "stock": stock
        }) #kitap bilgilerini bir sözlük olarak all_books listesine ekliyoruz

    #sonraki sayfa var mı kontrol et
    next_button = soup.find("li", class_="next")
    if next_button:
        page += 1
        time.sleep(0.6  ) #bir sonraki sayfaya geçmeden önce 0.6  saniye bekle, böylece sunucuya fazla yüklenmemiş oluruz
    else:
        break #son sayfa, kır döngüyü

#verileri csv dosyasına yazmak icin
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "price", "stars", "stock"])
    writer.writeheader() #csv dosyasına başlık satırını yaz
    writer.writerows(all_books) #tüm kitapları csv dosyasına yaz

print(f"Total {len(all_books)} books saved.")