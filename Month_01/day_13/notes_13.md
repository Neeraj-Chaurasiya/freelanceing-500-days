# 📅 Day 13 – Web Scraping with Multiple Pages

## ✅ Topics Covered

* **Target Website & Libraries**
* **Loop Through Multiple Pages**
* **Data Extraction (Title, Price, Rating)**
* **Store Data in CSV**
* **Practice Task**

---

## 1️⃣ Target Website & Libraries

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
```

* `requests` → Send HTTP requests to fetch HTML.
* `BeautifulSoup` → Parse HTML and extract data.
* `pandas` → Store data in tabular form (DataFrame) and save to CSV.
* `base_url` → Website pattern for multiple pages (`{}` → placeholder for page number).

---

## 2️⃣ Loop Through Multiple Pages

```python
titles = []
prices = []
ratings  = []

p = int(input("How many pages you hai to extract : "))
```

* Empty lists created for `titles`, `prices`, and `ratings`.
* `input()` → Ask user how many pages to scrape.
* `int()` → Convert input into integer.

```python
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
```

* `format(page)` → Insert page number in URL.
* `requests.get(url)` → Fetch that page’s HTML.
* `soup.find_all()` → Select all book containers.
* Extracted:

  * `title` → From `h3 > a` attribute.
  * `price` → From `<p class="price_color">`.
  * `rating` → From class attribute.

---

## 3️⃣ Store Data in CSV

```python
df = pd.DataFrame({"Title": titles, "Price": prices})
df.to_csv("books_multi_page.csv", index=False)
print("Saved multi-page data to books_multi_page.csv")
```

* Convert extracted lists into DataFrame.
* Save **Title + Price** into CSV file.
* `index=False` → Don’t save row numbers.

---

## 4️⃣ Small Practice Task 🚀

```python
df = pd.DataFrame({"Title": titles, "Price": prices, "Rating": ratings})
df.to_csv("books_full.csv", index=False)
print("Saved multi-page data to books_full.csv")
```

* Create another DataFrame with `Rating` column.
* Save complete data (`Title + Price + Rating`) into CSV.

---

## 5️⃣ Summary

* Used **requests + BeautifulSoup** to scrape multiple pages.
* Extracted **title, price, and rating** from each book.
* Stored scraped data into **DataFrame**.
* Saved data into **CSV files** (`books_multi_page.csv`, `books_full.csv`).
* **Key Functions**: `.format()`, `requests.get()`, `soup.find_all()`, `.to_csv()`.
