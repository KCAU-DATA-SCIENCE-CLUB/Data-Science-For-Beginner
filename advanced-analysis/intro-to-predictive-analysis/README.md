

# 🧮 **Lesson 2: More with Pandas — Grouping, Joining & Feature Engineering**

Pandas is the **Swiss Army knife of data analysis** in Python.
Once you’ve mastered loading and cleaning data, it’s time to **analyze, combine, and transform** it for deeper insights.

This lesson takes you beyond basics — into the **core tools** for summarizing, merging, and enhancing data for analysis.

---

## 📊 **1. Grouping Data — Finding Patterns**

Grouping lets you **aggregate** data based on categories.
It’s like asking: *“What is the average income per country?”* or *“How many customers did each branch serve?”*

### Example

```python
import pandas as pd

df = pd.DataFrame({
    'City': ['Nairobi', 'Nairobi', 'Kisumu', 'Mombasa'],
    'Sales': [200, 150, 300, 100]
})

grouped = df.groupby('City')['Sales'].sum()
print(grouped)
```

**Output:**

```
City
Kisumu     300
Mombasa    100
Nairobi    350
```

🧠 **Why it matters:**
Grouping helps uncover **trends and performance differences** across segments (like branches, months, or users).

---

### 🪄 Common Aggregations

| Function            | Description    | Example                      |
| ------------------- | -------------- | ---------------------------- |
| `.sum()`            | Adds up values | Total sales per region       |
| `.mean()`           | Finds averages | Average grade per student    |
| `.count()`          | Counts entries | Number of customers per city |
| `.max()` / `.min()` | Finds extremes | Highest revenue per store    |

---

## 🔗 **2. Joining & Merging Datasets**

In real-world projects, your data rarely lives in one file.
You’ll often need to **combine multiple datasets** — for instance, customers + purchases + locations.

### Example

```python
customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Brian', 'Cindy']
})

orders = pd.DataFrame({
    'OrderID': [101, 102, 103],
    'CustomerID': [1, 1, 2],
    'Amount': [250, 150, 300]
})

merged = pd.merge(customers, orders, on='CustomerID', how='inner')
print(merged)
```

**Output:**

```
   CustomerID   Name  OrderID  Amount
0           1  Alice      101     250
1           1  Alice      102     150
2           2  Brian      103     300
```

### 🧩 Join Types

| Join Type      | Description                   | Visual                                                                                                        |
| -------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Inner Join** | Keeps only matching rows      | ![Inner Join Diagram](https://raw.githubusercontent.com/dataprofessor/data/master/images/inner_join.png)      |
| **Left Join**  | Keeps all from left table     | ![Left Join Diagram](https://raw.githubusercontent.com/dataprofessor/data/master/images/left_join.png)        |
| **Outer Join** | Keeps all rows, fills missing | ![Outer Join Diagram](https://raw.githubusercontent.com/dataprofessor/data/master/images/full_outer_join.png) |

*(You can use ASCII diagrams or simple sketches if offline)*

---

## 🧩 **3. Feature Engineering — Creating New Insights**

Feature Engineering is the art of **turning raw data into meaning**.
It involves creating new columns that **help models learn better or make analysis easier.**

### Examples

| Goal                | Technique        | Example                                        |
| ------------------- | ---------------- | ---------------------------------------------- |
| Simplify categories | Binning          | Group ages into “Teen”, “Adult”, “Senior”      |
| Handle time         | Extract features | From “2023-01-01” → get “Year”, “Month”, “Day” |
| Measure ratios      | Derived features | `Revenue_per_User = Revenue / Users`           |
| Encode trends       | Rolling features | `7-day average of daily sales`                 |

### Example Code

```python
df['Revenue_per_User'] = df['Revenue'] / df['Users']
df['Month'] = pd.to_datetime(df['Date']).dt.month
```

🧠 **Why it matters:**
Features are the **DNA of analysis** — they shape how you interpret data or train models later.

---

## ⚙️ **4. Real-World Example — Netflix Dataset**

Imagine you’re analyzing Netflix titles.

You can:

* Group by *genre* to find the **most popular categories**
* Merge with ratings data for **audience insights**
* Create features like `release_decade` or `is_popular`

```python
genre_count = df.groupby('Genre')['Title'].count().sort_values(ascending=False)
```

**Insight:**

> “Drama and Comedy dominate Netflix’s library, together making up nearly 60% of titles.”

---

## 🎨 **5. Visual Summary**

Below is a conceptual flow of how this lesson connects together:

```
Raw Data
   ↓
Cleaning
   ↓
Grouping & Aggregation
   ↓
Merging Multiple Sources
   ↓
Feature Engineering
   ↓
Visual Analysis / Modeling
```

This is the typical **data transformation pipeline** you’ll repeat in nearly every data project.

---

## 🚀 **6. Activity — Analyze & Transform**

Choose a dataset (e.g., sales, Netflix, CO₂, or happiness).

Perform the following:

1. Group the data by one key category
2. Merge with another dataset (if possible)
3. Create **two new features**
4. Write a **1–2 sentence insight** for each transformation

Example:

> “Grouping sales by region revealed that 40% of total revenue came from the coastal area — merging with customer data showed that tourists made up 70% of those purchases.”

---

## 🧭 **7. Summary**

By now, you should be able to:
✅ Use Pandas `.groupby()` for aggregations
✅ Merge multiple datasets with joins
✅ Create new features to enrich analysis

> “Data cleaning makes data usable.
> Data transformation makes it powerful.”







﻿
