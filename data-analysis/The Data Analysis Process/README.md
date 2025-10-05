# 🔎 Lesson 2: The Data Analysis Process

Now that we know *what* Data Analysis is, let’s dive into the **process** of doing it step by step.
Think of it as a **journey from raw data → insights → decisions**.

---

## 🛠️ The 5 Steps of Data Analysis

| Step                           | What Happens                                                    | Example (E-commerce Store)                               |
| ------------------------------ | --------------------------------------------------------------- | -------------------------------------------------------- |
| **1. Collect**                 | Gather raw data from databases, APIs, surveys, logs.            | Website clicks, purchase history, customer demographics. |
| **2. Clean**                   | Fix missing values, duplicates, outliers, inconsistent formats. | Standardizing “M”/“Male”, removing duplicate user IDs.   |
| **3. Explore**                 | Use descriptive statistics & visuals to understand patterns.    | Plot sales trends by month, check top-selling products.  |
| **4. Analyze**                 | Apply deeper methods: correlations, tests, models.              | Finding if discounts increase repeat purchases.          |
| **5. Interpret & Communicate** | Translate findings into insights, reports, and recommendations. | Present: “Increase ads during weekends → +20% sales.”    |

---

## 📊 Visual Flow: Data Analysis Pipeline

```
   [ Collect ] → [ Clean ] → [ Explore ] → [ Analyze ] → [ Interpret ]
```

This pipeline keeps repeating, because **real-world data projects are iterative**, not one-time.

---

## 🧩 Key Notes on Each Step

### 1️⃣ Data Collection

* Sources: spreadsheets, APIs, sensors, web scraping.
* Tools: Python (requests, BeautifulSoup), SQL, Excel.
* Tip: Always document *where* data came from.

### 2️⃣ Data Cleaning

* Handle missing values (`NaN` in Pandas).
* Remove or fix outliers.
* Normalize formats (dates, currencies).

### 3️⃣ Data Exploration

* Summary stats: mean, median, min, max.
* Visuals: histograms, scatterplots, boxplots.
* Goal: **“Get a feel”** for the data.

### 4️⃣ Analysis

* Look for correlations, trends, clusters.
* Apply statistical methods or ML models (later modules).
* Example: “Do students who study more hours score higher?”

### 5️⃣ Interpretation & Communication

* Use visuals, dashboards, or reports.
* Tell the story: *What is the business or social implication?*
* Example: Instead of saying *“average = 25”*, say *“customers buy 25 items per week on average, which suggests…”*.

---

## 🌍 Real-World Example

**Case: Netflix User Behavior**

1. Collect → Watch history (movies, genres).
2. Clean → Remove corrupted logs, fix time zones.
3. Explore → Find top 5 most watched genres.
4. Analyze → Correlate binge-watching with subscription renewals.
5. Interpret → Recommend more shows in trending categories.

---

## ✅ Takeaway

The **Data Analysis Process = a pipeline** that ensures raw data becomes **clean, explored, and analyzed** before being communicated effectively.

👉 In the next lesson, we’ll explore **types of data & formats** (numerical, categorical, structured, unstructured) and why they matter.
