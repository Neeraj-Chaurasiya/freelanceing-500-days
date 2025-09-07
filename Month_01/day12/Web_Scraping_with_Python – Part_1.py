# ------------------------------ Libraries Install & Import -----------------------------------

import requests 
from bs4 import BeautifulSoup
import pandas as pd

# ----------------------------- Simple Web Request ------------------------------------

url = "https://books.toscrape.com/"
response = requests.get(url)
print(response.status_code)   

# --------------------------- Parse HTML with BeautifulSoup ---------------------------------

soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)

# --------------------------- Extract Multiple Elements ----------------------------------

books = soup.find_all("h3")
title = [book.a["title"] for book in books]
print(title)

# ---------------------------- Store Data in DataFrame & CSV ----------------------------

df = pd.DataFrame({"Books title ": title})
df.to_csv("Books.csv", index=False)
print("Saved to books.csv")

# ----------------------------- Practice Task 🚀 -----------------------------

books = soup.find_all("article",class_="product_pod")

titles = []
prices = []
ratings = []

for book in books:

  title = book.h3.a["title"]
  titles.append(title)

  price = book.find("p" , class_= "price_color").text
  prices.append(price)

  rating = book.p["class"][1]
  ratings.append(rating)

  df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings
  })

df.to_csv("boook_price.csv", index=False)
print("Data saced to book_price.csv")