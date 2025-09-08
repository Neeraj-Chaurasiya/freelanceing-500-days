# ----------------------------------- Target Website & Libraries ----------------------------

import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# -------------------------------------- Loop Through Multiple Pages ---------------------------

titles = []
prices = []
ratings  = []

p = int(input("How many pages you hai to extract : "))

for page in range(p):
  url = base_url.format(page)
  response = requests.get(url)
  soup = BeautifulSoup(response.text ,"html.parser")

  books = soup.find_all("article", class_="product_pod")

  for book in books:
    title = book.h3.a['title']
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]
    titles.append(title)
    prices.append(price)
    ratings.append(rating)

# -------------------------------------- Store Data in CSV --------------------------------------

df = pd.DataFrame({"Title": titles, "Price": prices})
df.to_csv("books_multi_page.csv", index=False)
print("Saved multi-page data to books_multi_page.csv")

# ----------------------------------- Small Practice Task 🚀 -------------------------------------

df = pd.DataFrame({"Title": titles, "Price": prices, "Rating": ratings})
df.to_csv("books_full.csv", index=False)
print("Saved multi-page data to books_full.csv")