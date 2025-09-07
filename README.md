# LEARNING DATA ANALYST STEP-BY-STEP.

# 📅 Day 1 – NumPy Basics

## ✅ Topics Covered
- Introduction to NumPy
- Creating arrays from Python lists
- Array attributes: `type`, `shape`
- Special arrays: `zeros`, `ones`, `eye`, `arange`, `linspace`
- Indexing & slicing (1D and 2D)

## 🎯 Practice Task
1. Create an array with numbers 1–20.  
2. Print only even numbers.  
3. Create a 4x5 matrix and print:  
   - 2nd row  
   - 3rd column  
   - Last element

---

# 📅 Day 2 – NumPy Operations & Matrix Handling

## ✅ Topics Covered
- Arithmetic operations on arrays (`+`, `-`, `*`, `/`, `**`)
- Mathematical & statistical functions:
  - `min`, `max`, `mean`, `median`, `std`, `sum`
- Reshape and axis-based operations
  - `reshape()`
  - `sum(axis=0)`, `sum(axis=1)`
- Random number generation
  - `np.random.rand`, `np.random.randint`, `np.random.seed`

## 🎯 Practice Task
1. Create a 3x3 random integer matrix (values 1–50).  
2. Print row-wise maximum and column-wise minimum.  
3. Create a 1D array (1–16), reshape to 4x4, then print:  
   - Row-wise sum  
   - Column-wise sum  

---

# 📅 Day 3 – Pandas Basics (Series & DataFrame)

## ✅ Topics Covered
- Introduction to **pandas** library  
- **Series (1D data)**  
  - Creating from list  
  - Custom index  
- **DataFrame (2D data)**  
  - Creating from dictionary  
  - Rows & columns overview  
- Basic DataFrame functions  
  - `head()`, `tail()`, `shape`, `info()`, `describe()`

## 🎯 Practice Task
1. Create a student DataFrame with 5 students → Columns: `Name, Age, Marks, City`.  
2. Print first 3 rows (`head(3)`).  
3. Check DataFrame shape and info.  
4. Calculate `Marks` ka mean aur max value.  

---

# 📅 Day 4 – Pandas Indexing, Selection & Filtering

## ✅ Topics Covered
- **Column selection**
  - `df["col"]` → single column (Series)
  - `df[["col1", "col2"]]` → multiple columns (DataFrame)
- **Row selection**
  - `iloc` → index-based (0,1,2…)
  - `loc` → label-based (row labels, specific columns)
- **Conditional filtering**
  - `df[df["Marks"] > 88]`
  - `df[(df["Age"] > 22) & (df["Marks"] >= 88)]`
- **Adding & dropping columns**
  - `df["new_col"] = ...`
  - `df.drop("col", axis=1)`

## 🎯 Practice Task
1. Ek **employee DataFrame** banao with columns: `EmpID, Name, Age, Department, Salary` (5 employees).  
2. Sirf `Name` aur `Salary` column print karo.  
3. Sirf un employees ko print karo jinki `Salary > 50,000` ho.  
4. Ek naya column **"Bonus"** add karo (Salary ka 10%).  
5. `"Department"` column drop karo.  

---

# 📅 Day 5 – Pandas GroupBy, Aggregate & Pivot Table

## ✅ Topics Covered
- **GroupBy basics**
  - `df.groupby("col")["target"].mean()`
- **Multiple aggregations**
  - `agg(["mean","max","min"])`
- **GroupBy with multiple columns**
  - `df.groupby(["col1","col2"])["target"].sum()`
- **Pivot tables**
  - `df.pivot_table(index="col", values="target", aggfunc="mean")`

## 🎯 Practice Task
1. Ek **sales DataFrame** banao with columns: `Region, Product, Sales, Profit` (8 rows).  
2. Group by `Region` → total **Sales** nikalo.  
3. Group by `Product` → average **Profit** nikalo.  
4. Ek **Pivot Table** banao jisme:
   - Rows = Region  
   - Columns = Product  
   - Values = Sales sum  

---

# 📅 Day 6 – Pandas Merge, Join & Concat

## ✅ Topics Covered
- **Concatenation**
  - `pd.concat([df1, df2])` → vertical (rows) combine
  - `pd.concat([df1, df2], axis=1)` → horizontal (columns) combine
- **Merge (SQL JOIN style)**
  - `pd.merge(df1, df2, on="col", how="inner")`
- **Different Types of Joins**
  - `how="left"` → Left Join
  - `how="right"` → Right Join
  - `how="outer"` → Full Outer Join
- **Join using Index**
  - `df1.join(df2, how="outer")`

## 🎯 Practice Task
1. Ek **students DataFrame** banao with columns:  
   `RollNo, Name, Class`.  
2. Ek **marks DataFrame** banao with columns:  
   `RollNo, Subject, Marks`.  
3. Merge karke ek final DataFrame banao jisme:  
   `Student Name + Subject + Marks` ho.  
4. Concatenate karke do alag batches ka students data ek hi DataFrame me lao.  

---

# 📅 Day 7 – Pandas GroupBy & Aggregation

## ✅ Topics Covered
- **Basic GroupBy**
  - `df.groupby("col")["val"].mean()` → group-wise average
- **Multiple Aggregations**
  - `agg(["mean","sum","max","min"])` → ek group ke multiple stats
- **GroupBy on Multiple Columns**
  - `df.groupby(["col1","col2"])["val"].mean()`
- **Sorting Aggregated Results**
  - `.sort_values(ascending=False)`

## 🎯 Practice Task
1. Ek **sales DataFrame** banao jisme columns ho:  
   `Region, Product, Sales`.  
2. `groupby()` karke har **Region ka total sales** nikaalo.  
3. Har **Product ka average sales** nikaalo.  
4. Top 1 product identify karo jo sabse zyada bikta hai.  

---

# 📅 Day 8 – Pandas Data Cleaning & Preprocessing

## ✅ Topics Covered
- **Missing Values**
  - `df.isnull()` → missing check
  - `df.dropna()` → drop missing rows
  - `df.fillna(value)` → fill missing values
- **Duplicates**
  - `df.duplicated()` → duplicate check
  - `df.drop_duplicates()` → remove duplicates
- **Rename + Replace**
  - `df.rename(columns={"old":"new"})`
  - `df["col"].replace(old, new)`
- **String Cleaning**
  - `.str.strip()` → trim spaces  
  - `.str.upper()` → uppercase  
  - `.str.title()` → title case  

## 🚀 Practice Task
1. Ek DataFrame banao jisme:
   - Kuch `NaN` values
   - Duplicate rows
   - Extra spaces in strings  
2. Data cleaning steps apply karke ek **final clean dataset** banao.  
3. GitHub pe upload karo: **pandas_cleaning_day8.ipynb**  

---

## ✅ Expected Output
Tumhe real-world **data cleaning pipeline** samajh aayega:
- Missing values handle karna
- Duplicates remove karna
- Columns rename/replace
- String strip/title/upper  

⚡ Ye freelancing aur industry projects me sabse zyada use hoti skill hai.  

---

# 📅 Day 9 – Exploratory Data Analysis (EDA – Part 1)

## ✅ Topics Covered
- **Dataset Load & Info**
  - `pd.read_csv()` → dataset import
  - `.head()`, `.info()`, `.describe()` → dataset samajhna
- **Univariate Analysis**
  - `.mean()`, `.value_counts()`, `.unique()` → single column analysis
- **Bivariate Analysis**
  - `.groupby()` → relation between two columns
- **Visualization (Matplotlib Basics)**
  - Histogram → distribution
  - Bar Plot → average comparison
  - Scatter Plot → relation between numeric columns

## 🚀 Practice Task
Dataset: **tips.csv**  
1. Find **highest tip kis day pe di gayi**  
2. Calculate **Male vs Female average bill difference**  
3. Scatter plot banao: `size` vs `total_bill`  

Upload: **eda_day9.ipynb** to GitHub.

---

## ✅ Expected Output
- Dataset ka **overview** samajh aayega  
- Univariate + Bivariate analysis clear hoga  
- Basic **EDA plots** (histogram, bar, scatter) seekh jaoge  

⚡ Ye har Kaggle project aur freelancing analysis ka **Step-1** hai.  

---

# 📅 Day 10 – Exploratory Data Analysis (EDA – Part 2, Seaborn)

## ✅ Topics Covered
- **Seaborn Setup**
  - `sns.histplot`, `sns.boxplot` → distribution + outliers
  - `sns.barplot`, `sns.countplot` → categorical comparison
  - `sns.scatterplot`, `sns.lineplot` → relationships
  - `sns.heatmap` → correlation matrix

## 📊 Visualizations
1. **Distribution Plots**
   - Histogram (total_bill)
   - Boxplot (bill per day)
2. **Categorical Plots**
   - Barplot (avg bill by day)
   - Countplot (gender count)
3. **Relationship Plots**
   - Scatterplot (bill vs tip, hue=sex)
   - Lineplot (bill by group size)
4. **Heatmap**
   - Correlation matrix

## 🚀 Practice Task
Dataset: **tips.csv**  
1. Male vs Female **average tip** ka barplot banao.  
2. Day-wise **bill distribution** ka boxplot banao.  
3. Heatmap banao aur identify karo → **tip ke saath sabse zyada correlated column** kaunsa hai.  

---

## ✅ Expected Output
- Distribution, categorical, relationship aur heatmap plots ka mastery.  
- Gender, day aur correlation-based analysis kar paoge.  
- EDA ke visualization step me confidence aayega 🚀  


# 📅 Day 11 – Mini Project: Sales Analysis

## ✅ Topics Covered
- Dataset Creation / Import (Superstore-style sales data)
- Data Cleaning:
  - Missing values check
  - Duplicate handling
  - String/category cleanup
- Exploratory Data Analysis:
  - Revenue calculation
  - Top-selling product
  - Region-wise sales
- Visualization (Seaborn + Matplotlib):
  - Product-wise sales (bar plot)
  - Region-wise sales (bar plot)
  - Correlation heatmap

---

## 🚀 Practice Task
1. Har **Region ka total revenue** nikalo.  
2. Identify karo **sabse zyada revenue generate karne wala product**.  
3. Ek **Bar Chart** banao → Product vs Revenue.  
4. Ek **Pie Chart** banao → Region-wise sales percentage.  

---

## ✅ Expected Output
- Tum ek **Mini Sales Analysis Project** complete kar loge.  
- Portfolio ke liye ek **freelancing-style analysis notebook** ready hoga.  
- Real-world workflow (Data Cleaning → EDA → Visualization → Insights) clear ho jayega 🚀  


# 📅 Day 12 – Web Scraping with Python (Part 1)

## ✅ Topics Covered
- **Libraries for Scraping**
  - `requests` → website ka HTML fetch karna
  - `BeautifulSoup` → HTML parse & extract
  - `pandas` → scraped data ko CSV me save karna
- **Basic Steps**
  - Send request → `requests.get(url)`
  - Parse HTML → `BeautifulSoup(html, "html.parser")`
  - Extract elements → `find_all("tag")`
  - Save to CSV with pandas

---

## 🚀 Practice Task
1. Website: **books.toscrape.com**  
   - Scrape book **title**, **price**, **rating**  
2. Data ko **DataFrame** me save karo  
3. Export CSV: **books_prices.csv**  
4. Upload on GitHub: **web_scraping_day12.ipynb**

---

## ✅ Expected Output
- Tum ek **basic web scraper** bana paoge.  
- Titles, prices, ratings jaisa **structured dataset** extract kar loge.  
- Freelancing ke liye ekdum useful skill (clients aksar data scraping mangte hain).  
- Next step: Pagination & multiple pages scrape karna (Day-13). 🚀  


# 📅 Day 13 – Web Scraping with Python (Part 2 / Advanced)

## ✅ Topics Covered

* **Advanced Scraping Concepts**

  * Pagination → multiple pages scrape karna
  * Looping through URLs → automate scraping
  * Extract multiple fields → title, price, rating
  * Store results in **lists** → then convert to DataFrame
* **Saving Data**

  * `pandas.DataFrame()` → structured data
  * `to_csv()` → export multiple-page data

---

## 🚀 Practice Task

1. Website: **books.toscrape.com**

   * Scrape **first 10 pages**
   * Extract: **title**, **price**, **rating**
2. Store all data in a **single DataFrame**
3. Export CSV: **books\_full.csv**
4. Upload on GitHub: **web\_scraping\_day13.ipynb**

---

## ✅ Expected Output

* Tum ek **multi-page web scraper** bana paoge
* Titles, prices, ratings jaisa **complete dataset** extract kar loge
* Freelancing ke liye **ready-to-use dataset** milega
* Next step: Scraped data ko **Pandas / Excel me clean & analyze** karna (Day-14) 🚀
