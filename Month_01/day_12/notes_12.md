# Web Scraping Notes

## 1️⃣ Libraries Install & Import

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
```

* `requests` → Fetch website HTML.
* `BeautifulSoup` → Parse HTML and extract data.
* `pandas` → Store data in DataFrame and save to CSV.

---

## 2️⃣ Simple Web Request

```python
url = "https://books.toscrape.com/"
response = requests.get(url)
print(response.status_code)
```

* `requests.get(url)` → Get webpage content.
* `response.status_code` → 200 = success, 404 = not found.

---

## 3️⃣ Parse HTML with BeautifulSoup

```python
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)
```

* `response.text` → HTML content.
* `BeautifulSoup(..., "html.parser")` → Parse HTML.
* `soup.title.text` → Print page title.

---

## 4️⃣ Extract Multiple Elements

```python
books = soup.find_all("h3")
title = [book.a["title"] for book in books]
print(title)
```

* `find_all("h3")` → Get all `<h3>` tags.
* `book.a["title"]` → Get book title from anchor tag.
* List comprehension → Create list of titles.

---

## 5️⃣ Store Data in DataFrame & CSV

```python
df = pd.DataFrame({"Books title ": title})
df.to_csv("Books.csv", index=False)
print("Saved to books.csv")
```

* `pd.DataFrame()` → Convert list to table.
* `to_csv()` → Save DataFrame to CSV.
* `index=False` → Exclude row indices.

---

## 6️⃣ Practice Task 🚀

```python
books = soup.find_all("article", class_="product_pod")
```

* Select each book block in the page.

```python
titles = []
prices = []
ratings = []
```

* Create empty lists for storing book data.

### Loop through each book:

```python
for book in books:
    title = book.h3.a["title"]
    titles.append(title)

    price = book.find("p", class_="price_color").text
    prices.append(price)

    rating = book.p["class"][1]
    ratings.append(rating)

    df = pd.DataFrame({
        "Title": titles,
        "Price": prices,
        "Rating": ratings
    })
```

* Extract `title`, `price`, `rating` for each book.
* Append to respective lists.
* Create/update DataFrame inside loop (for incremental view).

```python
df.to_csv("book_price.csv", index=False)
print("Data saved to book_price.csv")
```

* Save final DataFrame to CSV.
* `index=False` → Exclude row numbers.

---

## 7️⃣ Summary

* **Requests** → Get webpage HTML.
* **BeautifulSoup** → Parse HTML, extract tags & attributes.
* **Data Extraction** → Get book titles, prices, and ratings.
* **DataFrame & CSV** → Store extracted data and save to file.
* **Key Functions**: `requests.get()`, `soup.find_all()`, `tag["attribute"]`, `.text`, `pd.DataFrame()`, `.to_csv()`.
