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


# 📅 Day 14 – Scraped Data Cleaning & Analysis

## ✅ Topics Covered

* **Data Loading**

  * Import scraped CSV into pandas DataFrame
* **Data Cleaning**

  * Remove currency symbols & convert Price → numeric
  * Convert Rating (One–Five) → numeric scale (1–5)
  * Handle missing values / duplicates
* **Data Analysis**

  * Average price, highest priced book
  * Average rating
  * Grouping & aggregation
* **Visualization**

  * Price distribution (histogram)
  * Ratings count (bar chart)

---

## 🚀 Practice Task

1. Extract **Top 10 most expensive books**
2. Calculate **average price per rating** (1–5)
3. Create **bar chart** → Rating vs Average Price
4. Export cleaned dataset → **books\_cleaned.csv**
5. Upload notebook → **web\_scraping\_day14.ipynb**

---

## ✅ Expected Output

* Tum ek **scraped dataset ko clean & analyze** kar paoge
* Exported file: **books\_cleaned.csv** (ready for freelancing use)
* Clear **visual insights** (price trends, rating distribution)
* Next step (Day-15): **Automated Dashboard / Report (Excel / PowerBI)** 🚀

# 📅 Day 15 – Automated Dashboard / Report

## ✅ Topics Covered

* **Load Cleaned Dataset**

  * Import `books_cleaned.csv` into pandas DataFrame
* **Summary Metrics**

  * Total Books, Average Price, Average Rating
* **Visualizations**

  * Price Distribution (histogram)
  * Top 10 Expensive Books (bar chart)
  * Rating vs Average Price (bar chart)
* **Automated Excel Report**

  * Multiple sheets: All Books, Top 10 Expensive, Avg Price by Rating
  * Ready-to-share client deliverable

---

## 🚀 Practice Task

1. Display summary metrics: **Total Books, Average Price, Average Rating**
2. Plot: Price Distribution, Top 10 Expensive Books, Rating vs Average Price
3. Export **Excel report** with multiple sheets: `books_report.xlsx`
4. Upload notebook → **web\_scraping\_day15\_dashboard.ipynb**

---

## ✅ Expected Output

* Tum ek **automated dashboard / report** create kar paoge
* Cleaned dataset + plots + summary metrics **ek hi file / Excel report me ready**
* Freelancing ke liye **professional deliverable**
* Next step (Day-16): **Portfolio polishing + GitHub README / showcase ready** 🚀


# 📅 Day 16 – Portfolio & GitHub Showcase

## ✅ Topics Covered

* **Git & GitHub Basics**

  * Create repo → `git init`
  * Track changes → `git add .` + `git commit -m "message"`
  * Push to GitHub → `git push origin main`

* **README.md Polish**

  * Har project ke liye description likho
  * Structure: Problem → Approach → Solution → Output (screenshots / CSV / plots)

* **Portfolio Repo Structure**

  * Projects folder ke andar:

    * `Project_01_SalesAnalysis/`
    * `Project_02_WebScraping/`
    * `Project_03_Dashboard/`
  * Har project folder me ek `README.md` + code/data

* **GitHub Profile Setup**

  * Profile README banayo (intro + skills + contact)
  * Projects ko **pin** karo (Sales Analysis, Web Scraping, Dashboard)

---

## 🚀 Practice Task

1. GitHub profile me ek **professional repo structure** banao.
2. Har project ko **alag repo** me push karo.
3. Har repo ke liye ek **portfolio-style README.md** likho.
4. Profile README banao jisme tumhari **skills + projects + contact links** ho.

---

## ✅ Expected Output

* Ek **polished GitHub profile** jo tumhara portfolio show kare.
* Recruiters/clients ko lage ki tumne **real projects** kiye hain.
* Freelancing aur internship ke liye tumhari profile **ready-to-share** hogi. 🚀


# 📅 Day 17 – SQL Practice with SSMS (Sales Database)

## ✅ Topics Covered

* **Database Creation**
  * SSMS me ek naya Database banao → `SalesDB`
* **Table Creation**
  * Sales table with columns: id, product, category, price, quantity
* **Data Insertion**
  * Insert dummy product records (10–15 rows minimum)
* **Queries**
  * View all data (`SELECT *`)
  * Filtered data (`WHERE price > ...`)
  * Aggregation (`GROUP BY category → total revenue`)
* **Screenshots for Notes**
  * Queries + Outputs capture karke Day-17 notes.md me daalo

---

## 🚀 Practice Task

1. Create **SalesDB** database in SSMS  
2. Insert at least **10–15 sample product records**  
3. Run queries:
   * View all data
   * Filter products by price
   * Category-wise revenue calculation  
4. Take **screenshots of results** and add them in `Day-17/notes.md`  
5. Upload to GitHub → portfolio roadmap continue karo 🚀

---

## ✅ Expected Output

* Tum ek **Sales Database** SSMS me successfully bana loge  
* Basic SQL commands practice karoge: **CREATE, INSERT, SELECT, WHERE, GROUP BY**  
* Screenshots ke saath tumhare GitHub roadmap me ek **solid SQL practice proof** add ho jayega  
* Freelancing / interview ke liye tumhe **SQL confidence boost** milega ✅


# 📅 Day 18 – SQL Intermediate (Joins & Aggregations)

## ✅ Topics Covered

* **Customers Table Creation**
  * Ek alag table banakar customer details store karna  
* **Linking Tables**
  * `ALTER TABLE` se Sales aur Customers ko connect karna (via `customer_id`)  
* **Joins**
  * **INNER JOIN** → Sales + Customers ka matching data
  * **LEFT JOIN** → Sabhi customers ke sath unke sales records
* **Advanced Queries**
  * City-wise revenue calculation
  * Top 3 highest priced products

---

## 📂 Database Schema

**sales**  
- id  
- product  
- category  
- price  
- quantity  
- customer_id  

**customers**  
- customer_id  
- name  
- city  

---

## 🚀 Practice Task

1. `customers` table banao aur dummy records insert karo  
2. `sales` table ko update karo → `customer_id` ke sath link karo  
3. Queries run karo:
   * INNER JOIN → Sales + Customers ka combined data
   * City-wise revenue calculation  
   * Top 3 highest priced products  
4. Queries aur unke **screenshots** Day-18 `notes.md` me add karo  
5. Upload karo GitHub pe:  
   - `day18_sql_practice.sql` → queries  
   - `notes.md` → explanation + screenshots  
   - `README.md` → portfolio summary  

---

## ✅ Expected Output

* Tum **Joins (INNER + LEFT)** ka use samjhoge  
* City-wise & customer-wise revenue calculate kar paoge  
* Advanced filtering aur top-N queries likhna seekh jaoge  
* Freelancing clients ke liye **customer + sales linked reports** generate karna easy ho jayega  
* Portfolio me ek aur **professional SQL project** add ho jayega 🚀


# 📅 Day 19 – SQL Advanced Filtering & Functions

## ✅ Topics Covered

* **Advanced Filtering**
  * `WHERE` clause with conditions
  * `BETWEEN`, `IN`, `LIKE`, `IS NULL`
* **ORDER BY**
  * Multiple columns ke sath sorting (ASC / DESC)
* **SQL Functions**
  * **String Functions** → `LEN()`, `UPPER()`, `LOWER()`, `SUBSTRING()`
  * **Date Functions** → `GETDATE()`, `YEAR()`, `MONTH()`
  * **Numeric Functions** → `ROUND()`, `ABS()`

---

## 🚀 Practice Task

1. **Filtering Queries**
   * Price **1000 aur 50000 ke beech**
   * Product only `Laptop` ya `Phone`
   * Customers jinka naam `N` se start hota ho
   * Customers jinki **sales NULL** hai  

2. **Functions Practice**
   * Customer name length निकालना
   * Product ko `UPPERCASE` me dikhana
   * Price ko round off karna (nearest hundred)
   * Current date + Year extract karna  

3. **ORDER BY**
   * City wise ascending + Name wise descending sort  

4. Queries run karke screenshots `notes.md` me daalo  
5. Upload GitHub pe:
   - `day19_sql_practice.sql` → queries
   - `notes.md` → explanation + screenshots
   - `README.md` → portfolio roadmap summary  

---

## ✅ Expected Output

* Tum **filtering** ka mastery kar loge  
* **String, Date, Numeric functions** ka real-world use samjhoge  
* Data ko **clean & formatted** way me dikhana seekh jaoge  
* Freelancing ke liye client ke reports aur formatted SQL outputs banane me expert ban jaoge 🚀


# 📅 Day 20 – SQL Aggregations & Subqueries

## ✅ Topics Covered

* **Aggregate Functions**
  * `SUM()`, `AVG()`, `COUNT()`, `MAX()`, `MIN()`
* **GROUP BY**
  * Category / City wise totals
* **HAVING**
  * Aggregated groups pe condition lagana
* **Subqueries**
  * Ek query ke andar dusri query (nested queries)

---

## 🚀 Practice Task

1. **Aggregate Functions**
   * Total revenue (`SUM`)
   * Average product price (`AVG`)
   * Number of customers (`COUNT`)
   * Max & Min product price (`MAX`, `MIN`)

2. **GROUP BY + HAVING**
   * City-wise total revenue calculate karo
   * Sirf wahi cities show karo jinka revenue **50,000 se zyada** ho

3. **Subqueries**
   * Products jo **average price se zyada costly** hain
   * Customers jinhone **Laptop purchase kiya** hai

4. Queries run karke screenshots `notes.md` me daalo  
5. Upload GitHub pe:
   - `day20_sql_practice.sql` → queries
   - `notes.md` → explanation + screenshots
   - `README.md` → portfolio roadmap summary  

---

## ✅ Expected Output

* Tum **aggregation reporting** kar paoge  
* **City/Product wise summaries** easily generate kar paoge  
* **Subqueries** ki help se complex problems solve karna aa jayega  
* Freelancing aur interviews ke liye **professional SQL reporting skills** develop ho jayegi 🚀


# 📅 Day 21 – SQL Views, Indexes & Stored Procedures

## ✅ Topics Covered
* **Views** → Reusable queries banane ke liye  
* **Indexes** → Query performance fast karne ke liye  
* **Stored Procedures** → Queries ko automate karne ke liye  

---

## 🚀 Practice Queries

### 🔹 Views
* City-wise revenue ka ek **View** banao aur use query me reuse karo

### 🔹 Indexes
* Customers table ke `City` column pe index add karo  
* Sales table ke `Product` column pe index add karo  

### 🔹 Stored Procedures
* Ek stored procedure banao jo **Top N products by revenue** return kare  
* Procedure ko execute karke output verify karo  

---

## 📂 Files
* `day21_queries.sql` → saare SQL queries  
* `outputs/` → screenshots ya exported CSVs  

---

## ✅ Expected Output
* Tum ek **View** bana paoge jo multiple reports me reuse hoga  
* **Indexes** ki wajah se queries fast execute hongi  
* **Stored Procedure** se tum automated reports generate kar paoge  

---

## 🌟 Portfolio Value
✔ Adds **professional database skills** (freelancing & jobs me high demand)  
✔ Shows you can **optimize queries** with indexes  
✔ Proof that you can **automate reporting** with stored procedures 🚀  


# 📅 Day 22 – SQL Advanced Joins, Nested Queries & Constraints

## ✅ Topics Covered
* **Self JOIN** → ek hi table ke andar join  
* **FULL OUTER JOIN** → dono tables ka complete data  
* **Nested Subqueries** → query ke andar query  
* **Constraints** → data ko validate karne ke liye  
  - NOT NULL  
  - UNIQUE  
  - CHECK  
  - DEFAULT  

---

## 🚀 Practice Tasks

### 🔹 Self JOIN
* Customers table me **self join** karke same city ke customers find karo  

### 🔹 FULL OUTER JOIN
* Sales aur Customers ka **full outer join** karke dono tables ka data combine karo  

### 🔹 Nested Subqueries
* Customers identify karo jinhone **average price se zyada ke products** kharide hain  

### 🔹 Constraints
* Ek `Employees` table banao with constraints:  
  - `NOT NULL` → Name  
  - `UNIQUE` → Email  
  - `CHECK` → Age >= 18  
  - `DEFAULT` → City = 'Unknown'  

---

## 📂 Files
* `day22_queries.sql` → saare SQL queries  
* `outputs/` → screenshots ya exported CSVs  

---

## ✅ Expected Output
* Tum **advanced joins** use karke complex data analysis kar paoge  
* **Nested queries** se complex reports generate kar paoge  
* **Constraints** se tum data integrity maintain karna seekh jaoge  

---

## 🌟 Portfolio Value
✔ Proof ki tum **complex joins** aur **subqueries** handle kar sakte ho  
✔ Freelancing ke liye **data validation + integrity rules** apply karna aata hai  
✔ Adds strong SQL concepts (industry me high demand) 🚀  


# 📅 Day 23 – SQL Aggregations & Window Functions

## 📌 Overview
Day-23 me maine **Advanced SQL Reporting & Analytics** cover kiya jisme aggregation aur window functions use karke professional level queries banayi.  
Ye skills freelancing, data analytics, aur real-world reporting ke liye directly useful hain.  

---

## ✅ Topics Mastered
- **Aggregate Functions** → SUM(), AVG(), COUNT(), MIN(), MAX()  
- **GROUP BY** → category / city wise data grouping  
- **HAVING** → aggregated data par conditions lagana  
- **Window Functions**  
  - ROW_NUMBER() → row-wise numbering  
  - RANK() → ranking based on sales  
  - PARTITION BY → customer/product wise segmentation  
  - AVG() OVER() → overall average ke sath comparison  


# 📅 Day 25 – SQL Correlated Subqueries & Conditional Logic

## 📌 Overview
Day-25 me maine **advanced SQL querying techniques** seekhe jo **dynamic reports aur business insights** ke liye use hote hain.  
Isme focus tha **Correlated Subqueries** (row-by-row comparison) aur **CASE WHEN** (conditional reporting).  

---

## ✅ Topics Mastered
- **Correlated Subqueries** → Subquery jo har row ke liye outer query ke context me run hoti hai  
- **CASE WHEN (Conditional Logic)** → Queries me IF-ELSE type decision making  
- **Subquery + CASE combo** → Smart reporting & business insights ke liye powerful approach


# 📅 Day 26 – SQL Transactions & ACID Properties

## 📌 Overview
Day-26 me maine **transactions aur ACID principles** master kiye, jo **financial systems, ecommerce aur banking applications** ke liye backbone hote hain.  
Transactions ensure karte hain ki multiple operations **ya to saath me complete ho ya cancel ho jaye** → data hamesha safe aur consistent rahta hai.  

---

## ✅ Topics Mastered
- **Transactions (BEGIN, COMMIT, ROLLBACK)** → All-or-Nothing execution  
- **ACID Properties**  
  - Atomicity → Sabhi steps execute ho ya koi nahi  
  - Consistency → Database valid state me rahe  
  - Isolation → Parallel transactions ek dusre ko disturb na kare  
  - Durability → Commit ke baad data permanent  
- **Savepoints** → Transactions ke beech checkpoints  
- **Isolation Levels** → Transactions ke concurrency control  

---

# 📅 Day 27 – SQL Triggers (AFTER & INSTEAD OF)

## 📌 Overview
Day-27 me maine **SQL Triggers** master kiye.  
Triggers wo **automatic actions** hote hain jo INSERT, UPDATE, DELETE par run hote hain.  
Isse databases khud apne aap **audit logs maintain**, **data validation**, aur **auto-calculations** kar sakte hain – bina manual code likhe.

---

## ✅ Topics Mastered
- **Trigger Basics** → Auto execution on data changes  
- **AFTER Triggers** → Action hone ke baad run hote hain (e.g. audit logs)  
- **INSTEAD OF Triggers** → Original action replace hota hai custom logic se  
- **Use Cases** →  
  - Audit trails maintain karna  
  - Automatic calculations  
  - Data validation & restrictions  

---

# 📅 Day 28 – SQL User Roles & Permissions (Database Security)

## 📌 Overview
Day-28 me maine **SQL Database Security** ke core concepts master kiye.  
Ab mai samjh gaya hoon kaise database me **users, roles aur permissions** control karte hain —  
taaki **unauthorized access** aur **data misuse** na ho.

---

## ✅ Topics Mastered
- **Database Security Basics** → Users, Roles, Permissions ka concept  
- **User Management** → Login aur Database User creation  
- **Roles** → Predefined roles (db_datareader, db_datawriter, db_owner)  
- **Permissions Control** → GRANT, REVOKE, DENY commands  
- **Practical Use Cases** →  
  - Clients ko **read-only access** dena  
  - Developers ke liye **restricted editing rights**  
  - Database safety aur compliance maintain karna  

---

# 📅 Day 29 – SQL Optimization & Query Performance

## ✅ Topics Covered
- **Query Execution Plan (EXPLAIN / SHOWPLAN)** → Query engine ka behavior samajhna  
- **Indexes (Clustered vs Non-Clustered)** → Fast data retrieval ke liye indexing  
- **Performance Analysis** → Execution time aur plan comparison  
- **Optimization Techniques**  
  - Efficient **JOINs** vs **Subqueries**  
  - Use of **CTEs** for better readability  
  - Avoiding unnecessary SELECT *  
  - Dropping unused indexes for write optimization  
- **Composite Indexes** → Multi-column search optimization  
- **Real-time Performance Testing** using `SET STATISTICS TIME`  
- **Best Practices** → Query structure tuning for scalability  

---

## 🌟 Portfolio Value
- ✅ Demonstrates **Advanced SQL Performance Optimization** expertise  
- ✅ Proof that you can **analyze execution plans** and make queries faster  
- ✅ Shows capability to handle **large-scale datasets efficiently**  
- ✅ Adds **high-value technical depth** — demanded by top companies (Google, Amazon, Flipkart, etc.)  
- ✅ Freelancing edge: build **faster dashboards & analytics systems** for clients  
- ✅ Reinforces you as a **professional SQL developer** who understands backend performance tuning  

---

# 📅 Day 30 – Mini Project: E-Commerce Database Analysis (End-to-End SQL Case Study)

## 🎯 Objective
Build a **real-world SQL Case Study** on *E-Commerce Sales Data* to perform  
business analysis using **advanced SQL concepts** like joins, subqueries, views, procedures, and triggers.

---

## ✅ Topics Covered
| Concept | Description |
|----------|-------------|
| **Database Design** | Created tables for `Customers`, `Products`, and `Sales` |
| **Joins** | Combined data across tables for analysis |
| **Aggregations** | Calculated revenue, top products, category-wise sales |
| **Subqueries** | Used for comparative data logic |
| **Views** | Created reusable summary queries (Customer Sales Summary) |
| **Stored Procedures** | Automated city-wise sales reports with parameters |
| **Triggers** | Added automation to log/notify after inserts |
| **Filtering & Grouping** | Analyzed sales within date ranges and categories |
| **Portfolio-Ready Project** | Complete dataset + insights + automation setup |

🧠 Concepts Reinforced

✅ Relational Database Design

✅ Data Aggregation & Filtering

✅ Views & Procedures for Reusability

✅ Automation with Triggers

✅ Real-world Query Logic & Reporting

💼 Final Outcome

By the end of Day 30, you will have:

A fully functional SQL project simulating an e-commerce analytics system

Skills in real-world database automation and reporting

A portfolio-ready GitHub project demonstrating your SQL proficiency

Resume line to add:

“Built an end-to-end SQL case study analyzing e-commerce sales using advanced database concepts (joins, procedures, triggers, and performance optimization).”

🌟 Portfolio Value

✔ Demonstrates end-to-end SQL capability (design → logic → automation)
✔ Looks impressive to recruiters and freelance clients
✔ Perfect for Data Analyst / SQL Developer interviews
✔ Adds real project proof to your GitHub profile 🚀

--

# 📅 Day 31 – Python + SQL Integration (Data Fetching & Analysis)

## 🎯 Objective
Connect **SQL Server** with **Python (pandas)** to fetch, analyze, and export real business data.  
Ye freelancing aur data analytics projects ka sabse common real-world workflow hai 💼  

---

## ✅ Topics Covered
- **Database Connection (pyodbc)** → Secure connection between Python & SQL Server  
- **Data Extraction (SQL Queries)** → Fetch live data directly into Python  
- **Data Conversion (pandas)** → Convert query result into a DataFrame  
- **Data Analysis**  
  - Customer-wise revenue summary  
  - Product/category performance  
- **Excel Export (openpyxl)** → Save insights as client-ready reports  
- **Integration Workflow** → SQL + Python combo for automation & dashboards  

---

## 🧩 Pre-Setup
- ✅ SSMS me `ECommerceDB` database ready (Day-30 project se)  
- ✅ Python environment active (VS Code / venv)  
- ✅ Dependencies install:
  ```bash
  pip install pyodbc pandas openpyxl

---

# 📅 Day 32 – Data Analysis & Visualization using SQL Data (Python + Pandas + Matplotlib)

## 🎯 Objective
SQL se fetched data ko Python me analyze, clean, aur visualize karna.  
Ye freelancing aur data analyst jobs dono ke liye **core, real-world skill** hai.  

---

## ✅ Topics Covered
- **Data Cleaning using pandas** → Missing values, duplicates, and structure check  
- **Aggregation & Grouping** → City-wise, Category-wise revenue analysis  
- **Visualization using Matplotlib & Seaborn** → Interactive charts for insights  
- **Data Export** → Cleaned + visualized reports exported to Excel  
- **SQL-Python Integration** → Combining database logic with analytical visualization  

---

# 📅 Day 33 – Power BI Dashboard (Part 1): Connect & Model Data

## 🎯 Objective
Learn how to connect **SQL Server Database (ECommerceDB)** to **Power BI**, clean and model data for dashboard creation.  
Ye foundation hai ek **dynamic business dashboard** banane ke liye (real-world client style setup). 💼  

---

## ✅ Topics Covered
- **Power BI Interface Overview**  
- **SQL Server Connection** – Import live data from SQL  
- **Data Modeling** – Define relationships between tables  
- **Data Cleaning (Power Query Editor)** – Rename, remove, format & transform columns  
- **Calculated Columns** – Add business logic (e.g., Total Sales = Quantity × Price)  
- **Data Model Validation** – Verify correct relationships between tables  

---

## 🧩 Pre-Setup
- 🟢 Install Power BI Desktop  
  👉 Download: [https://powerbi.microsoft.com/desktop](https://powerbi.microsoft.com/desktop)  
- 🟢 Ensure your SQL Server Database `ECommerceDB` is ready (from Day 30)  
- 🟢 Tables required: **Customers**, **Products**, **Sales**  

---

# 📅 Day 34 – Power BI Dashboard (Part 2): Visual Design & Insights

## 🎯 Objective
SQL Server se imported data ka use karke **Power BI me interactive dashboard** banana.  
Dashboard me include honge:  
- **Revenue by City**
- **Top Products**
- **Category-wise Sales Trends**
- **Key KPIs (Revenue, Sales, Customers)**  

Ye tumhara **first professional Power BI dashboard project** hoga —  
jo **GitHub + LinkedIn portfolio** ke liye perfect hai 💼  

---

## ✅ Topics Covered
- **Creating Visuals in Power BI**
  - Bar, Pie, Line, and Column charts
- **Revenue & Product Performance**
  - Total Revenue, Top Products, Category Sales
- **KPI Cards**
  - Total Revenue, Total Sales, Unique Customers
- **Interactive Filters (Slicers)**
  - City, Product Category, Date Range
- **Dashboard Formatting & Theme**
  - Consistent colors, alignment, title text & layout design  

---

# 📅 Day 35 – Power BI Project Export & Portfolio Upload

## 🎯 Objective
Apna Power BI dashboard (from **Day 34**) final polish, export, aur **GitHub + LinkedIn** par upload karna.  
Isse tumhara **first professional portfolio project** ready ho jaayega:  
> 🧠 “E-Commerce Sales Dashboard using Power BI + SQL”

---

## ✅ Topics Covered
- **Power BI Export Formats**
  - `.PBIX` (editable dashboard file)
  - `.PDF` (for portfolio presentation)
  - `.PNG` (dashboard snapshot for GitHub/LinkedIn)
- **GitHub Project Setup**
  - Folder structure and `README.md`
  - Upload final project files and screenshots
- **LinkedIn Post Preparation**
  - How to present your dashboard project professionally
- **(Optional)** Power BI Service Publish (cloud sharing)

---

# 📅 Day 36 – Pandas Deep Dive (Part 1): Introduction & Data Loading

## 🎯 Objective  
Learn how to handle structured data using **Pandas** — the foundation of every data analysis project. 🚀  

## ✅ Topics Covered  
- What is Pandas & why it’s used  
- Series vs DataFrame (1D & 2D structures)  
- Import data → `read_csv()`, `read_excel()`  
- Explore data → `head()`, `info()`, `describe()`  
- Check missing → `isnull().sum()`  
- Clean & export → `to_csv()`  

💡 Outcome: You’ll be ready to **load, inspect, and clean** real datasets in Python.  

---

# 📅 Day 37 – Data Analysis & Aggregations with Pandas

## 🎯 Objective  
Learn to **analyze, group, and summarize** large datasets in Python using **Pandas**.  
Perform real-world business analysis on your `ecommerce_sales_34500.csv` dataset. 📊  

---

## ✅ Topics Covered  
- Data **filtering** with conditional logic (`df[df["Price"] > 50000]`)  
- **Sorting** values (`sort_values()`) for top/bottom records  
- **Grouping data** using `groupby()` (e.g., city-wise or category-wise sales)  
- **Aggregations** — `sum()`, `mean()`, `count()`, `max()`, `min()`  
- **Multiple aggregations** using `agg()` for combined insights  
- **Value counts** to check most frequent products/customers  
- **Unique values** to find diversity in data  
- Sorting aggregated results by revenue or count  
- Exporting final summarized reports with `to_csv()`  

---

## 💡 Outcome  
You’ll be able to:  
✔ Generate **business summaries** (sales by city/category)  
✔ Extract **top-performing products & regions**  
✔ Create **client-ready summary reports** using Pandas  
✔ Build the foundation for **data-driven decision making** 🚀  

---

# 📅 Day 38 – Data Visualization with Matplotlib & Seaborn

## 🎯 Objective  
Convert aggregated sales data into **insightful, professional visuals** for business storytelling and decision-making. 📊  

---

## ✅ Topics Covered  
- **Matplotlib Basics:** bar, line, pie charts  
- **Seaborn Advanced Visuals:** heatmap, boxplot, countplot  
- Custom color palettes & annotations  
- Dashboard-style themes (`sns.set_style("whitegrid")`)  
- Export visuals as `.png` files  
- Create mini visualization report (`notes_38.md`)  

---

## 🚀 Key Visuals  
1. **Total Sales by Category** → Bar chart  
2. **Average Sales by Region** → Horizontal bar  
3. **Quantity Comparison** → Line plot  
4. **Correlation Heatmap** → Sales metrics relationship  

---

# 📅 Day 39 – NumPy Deep Dive (Arrays, Math & Performance)

## 🎯 Objective  
Understand how **NumPy** works internally and why it’s the **foundation for Pandas & Machine Learning**.  
Focus: Array operations, broadcasting, and performance benchmarking ⚡  

---

## ✅ Topics Covered  
- **NumPy Setup & Basics** → Import, version check  
- **Array Creation** → `array()`, `zeros()`, `ones()`, `arange()`, `linspace()`  
- **Indexing & Slicing** → Access & subset array data  
- **Vectorized Operations** → Fast math without loops  
- **Broadcasting** → Handle arrays of different shapes  
- **Statistical Functions** → `mean()`, `max()`, `sum()`  
- **Performance Test** → Python list vs NumPy speed comparison  

---

## 🚀 Practice Tasks  
1️⃣ Generate random arrays: `price`, `quantity`, `discount`  
2️⃣ Compute `total_sale`, `final_sale`, `profit_margin`  
3️⃣ Find **average profit**, **max sale**, **total revenue**  
4️⃣ Compare execution time between **list** & **NumPy array**  
5️⃣ Save outputs in:  
   - `Month_02/day_39/numpy_basics.py`  
   - `Month_02/day_39/notes_39.md`  

---

## 🌟 Outcome  
✔ Master NumPy fundamentals & speed advantage  
✔ Perform vectorized math & array analytics  
✔ Benchmark performance for portfolio proof 🚀  

---

# 📅 Day 40 – Mini Project: Sales Data Report (Python + SQL)

## 🎯 Objective  
Build an **end-to-end Sales Data Analysis Project** using **Python + SQL + Visualization**.  
This marks the final output of **Phase 2A** — a real-world analytics project ready for your portfolio 💼  

---

## ✅ Topics Covered  
- Importing & cleaning data using **Pandas**  
- Handling missing values, duplicates & type conversion  
- **Feature engineering:** profit & final amount calculation  
- Business summaries using **groupby() & aggregation**  
- Creating professional charts with **Matplotlib & Seaborn**  
- Connecting to **SQL Server** with `pyodbc`  
- Exporting results to **Excel reports**  
- Building a client-ready analytics report  
- Automating insights generation  
- Preparing project for **GitHub & LinkedIn showcase**  

---

## ✅ Project Overview  
**Goal:**  
Analyze eCommerce sales data to extract business insights like **region-wise revenue**, **category profit**, and **customer behavior**.

**Tools Used:**  
- 🐍 Python  
- 📊 Pandas  
- 📈 Matplotlib / Seaborn  
- 🗄️ SQL Server (SSMS)  

**Dataset:**  
`ecommerce_sales_34500.csv`  

---

# 📊 Day 41 – Excel Power Query (Import, Clean & Transform Data)

A complete hands-on project using **Excel Power Query** to **import, clean, and transform raw eCommerce data**.  
This marks your transition from **Python + SQL analysis** to **Excel & Power BI data preparation** —  
the most common step in real-world business analytics workflows 💼  

---

## 🎯 Objective
Learn how to use **Excel Power Query** to handle messy raw data:
- Import large datasets directly into Excel
- Perform data cleaning and transformations  
- Prepare an **analysis-ready dataset** for Power BI or Excel Dashboards  

---

## ✅ Topics Covered
- **Power Query Basics** — Understanding Excel’s data transformation engine  
- **Importing Data** — From CSV, Excel, or SQL  
- **Cleaning Columns** — Remove unnecessary data, fix headers  
- **Changing Data Types** — Numeric, Date, Text conversions  
- **Calculated Columns** — Create “Final Amount = Price × Quantity × (1 - Discount)”  
- **Grouping & Sorting** — Aggregate and sort data by Region/Category  
- **Remove Duplicates & Replace Values**  
- **Export Clean Data** — Save final version back to Excel  

---

# 📊 Day 42 – Excel Formulas for Analysis (SUMIFS, VLOOKUP, INDEX-MATCH)

A practical Excel project focusing on **data analysis, lookup, and automation formulas**  
used daily by **data analysts, freelancers, and business professionals** 💼  

This project transforms cleaned sales data (from Day 41) into **insightful summary tables and reports** using Excel’s most powerful formulas.

---

## 🎯 Objective
Learn Excel ke advanced analytical formulas for:
- **Summarization** (SUMIFS, COUNTIFS, AVERAGEIFS)
- **Data Lookup** (VLOOKUP, INDEX-MATCH)
- **Conditional Logic** (IF, IFS)
- **Dynamic Reporting** (Multi-condition tables for analysis)

---

## ✅ Topics Covered
- **SUMIFS()** → Multi-condition total  
- **COUNTIFS()** → Multi-condition count  
- **AVERAGEIFS()** → Conditional average calculation  
- **VLOOKUP()** → Lookup based on key column  
- **INDEX + MATCH** → Flexible lookup alternative to VLOOKUP  
- **IF() / Nested IF() / IFS()** → Logical decision-making  
- **Formula Combinations** → Build real business summaries  

---

# 📅 Day 43 – Excel Charts + Interactive Dashboard (Professional Level)

Create a **fully interactive, client-ready Excel Sales Dashboard** using Pivot Tables, Charts,  
Slicers, and KPI cards.  
This is one of the most important skills for **data analysts, freelancers, and reporting jobs** 💼📊

---

## 🎯 Goal
Transform raw eCommerce sales data into a **dynamic Excel dashboard** containing:
- Revenue charts  
- Category trends  
- Region analysis  
- Payment method distribution  
- Interactive slicers  
- KPI summary cards  

---

## 📅 Day 44 – Power BI Data Modeling & DAX Basics

### ✅ Topics Covered
- Data Modeling fundamentals in Power BI  
- Star Schema architecture (Fact & Dimension tables)  
- Fact Table vs Dimension Tables concept  
- Creating relationships between tables  
- Understanding Cardinality (One-to-Many)  
- Cross Filter Direction (Single direction best practice)  
- Avoiding common modeling mistakes (Many-to-Many, circular relationships)  
- Creating basic DAX Measures:
  - Total Sales
  - Total Quantity
  - Total Orders
  - Total Customers
  - Average Profit Margin  
- Using a disconnected table for DAX Measures (best practice)  
- Validating and optimizing the data model  

---

## 📅 Day 45 – Power BI Visualization Mastery

### ✅ Topics Covered
- KPI Cards creation:
  - Total Sales
  - Total Orders
  - Total Customers
  - Average Profit Margin  
- Category-wise Sales visualization (Column Chart)  
- Region-wise Sales comparison (Bar Chart)  
- Monthly Sales Trend analysis (Line Chart)  
- Quantity / Orders based insights (Volume analysis)  
- Interactive Slicers:
  - Region
  - Category
  - Year
  - Payment Method  
- Dashboard interactivity using slicers  
- Professional dashboard layout & alignment  
- Formatting best practices:
  - Consistent color theme
  - Clean background
  - Readable titles & labels
- Designing client-ready, portfolio-level dashboards  
- Business-focused visualization thinking  

---

📅 Day 46 – Power BI Automation & Optimization

- Learned data refresh concepts (manual & scheduled)
- Optimized data model & measures
- Improved report layout & formatting
- Prepared dashboard for client delivery (PDF / PPT)

Outcome:
A clean, optimized, and client-ready Power BI dashboard.

---

# 📅 Day 47 – Power BI Project: Interactive Sales Insights Dashboard

## ✅ Topics Covered

- End-to-End Power BI Project Development
- KPI Cards Creation
  - Total Sales
  - Total Quantity
  - Total Orders
  - Average Profit Margin
- Business-Focused Visuals
  - Category-wise Sales Analysis
  - Region-wise Sales Analysis
  - Month-wise Sales Trend
  - Quantity Analysis by Category
- Slicers for Interactivity
  - Category
  - Region
  - Year
  - Payment Method
- Cross-Filtering & Interactions
- Dashboard Layout & Alignment
- Professional Formatting & UI Polish
- Client-Ready Dashboard Design
- Portfolio-Level Power BI Project Finalization

---

# 📅 Day 48 – Python + Power BI Integration

## ✅ Topics Covered

- Python-based data automation pipeline  
- Using the same raw dataset for processing  
- Data cleaning using Pandas  
- Business logic implementation (final amount calculation)  
- Generating processed & aggregated CSV files  
- Python as a data processing engine  
- Power BI connection with Python-generated CSV  
- Automated data refresh workflow concept  
- Separation of data layer (Python) and visualization layer (Power BI)  
- Real-world client-style Python + BI integration  

---

# 📅 Day 49 – Portfolio Project Setup

## ✅ Topics Covered

- Creating a **professional GitHub repository** for a data analytics project  
- Structuring a **portfolio-ready project folder** (data, scripts, dashboard, screenshots)  
- Preparing a **client / recruiter friendly repository layout**  
- Organizing **Power BI dashboard files** for public showcase  
- Managing **dataset versioning** for dashboard updates  
- Adding **Python automation script** for data refresh  
- Using **screenshots** to visually present dashboard insights  
- Writing a clean **README.md** for one-link project explanation  
- Applying **GitHub topics/tags** for better project visibility  
- Converting a learning dashboard into a **professional portfolio project**

---

## 🎯 Outcome

- One **single GitHub link** to showcase complete dashboard work  
- Clear separation of **data, code, visuals, and dashboard file**  
- Project ready for **freelancing proposals, internships, and recruiter reviews**  

---

## 📅 Day 49 – Portfolio Project Setup (GitHub)

### ✅ Topics Covered
- Creating a **professional GitHub repository**
- Designing a **clean and scalable folder structure**
- Separating code into:
  - Python scripts
  - Power BI files
  - Data files
- Writing a **portfolio-style README**
- Defining project **features, tech stack, and use case**
- Making the repository **client/recruiter friendly**
- Understanding how a clean repo improves credibility

---

## 📅 Day 50 – Review, Polish & Final Showcase

### ✅ Topics Covered
- Capturing **Power BI dashboard screenshots**
- Organizing screenshots for documentation
- Enhancing README with **dashboard preview section**
- Final **README polish** for public sharing
- Preparing **LinkedIn-ready project content**
- Understanding end-to-end project storytelling
- Converting a learning project into a **portfolio asset**
- Final review of Python + Power BI workflow

---

# 📅 Day 51 – Freelancing Reality + Platform Understanding

## 🎯 Objective
- Freelancing ka real-world mindset samajhna
- Client thinking aur project flow ko observe karna
- Long-term freelancing foundation build karna

---

## ✅ Topics Covered

- Freelancing Reality Check (Myths vs Reality)
- Beginner Freelancers ki Common Mistakes
- Freelancing Mindset (Skill > Degree, Portfolio > Certificate)
- Freelancing Platforms Overview
  - Upwork
  - Fiverr
  - Freelancer.com
- Client Job Post Analysis
- Budget Range & Project Expectations
- Skills → Client Keywords Mapping
- Profile Structure Observation
  - Profile photo style
  - Title format
  - Description tone
  - Portfolio section
- Freelancing Folder & File Setup
- Platform-wise Market Understanding

---

## 📁 Files & Setup
- notes.md → Freelancing learnings & mindset notes
- platforms_observed.txt → Platform comparison & observations
