# 📚 Lesson 3: Types of Data & Formats

Not all data is created equal. To analyze data effectively, you must first understand what kind of data you’re working with. Think of data as different *building blocks* — some are numbers, some are categories, some are time-based logs. How we analyze them depends on what type they are.

---

## 🧩 Types of Data

1. **Structured Data**

   * Organized in rows & columns (like an Excel sheet).
   * Examples: sales records, student grades, banking transactions.

2. **Unstructured Data**

   * No fixed format; messy and harder to store.
   * Examples: images, audio, free-text reviews, social media posts.

3. **Semi-Structured Data**

   * In between structured and unstructured.
   * Examples: JSON, XML, log files.

---

## 🔢 Levels of Data (Data Measurement Scales)

1. **Nominal** → Categories without order (e.g., gender, colors, city names).
2. **Ordinal** → Categories with order, but no exact difference (e.g., small/medium/large, survey ratings).
3. **Interval** → Numerical with meaningful differences but no true zero (e.g., temperature in °C).
4. **Ratio** → Numerical with a true zero, allows full math (e.g., height, weight, income).

📊 **Visual Example:**

```
Nominal   → ["Red", "Blue", "Green"]  
Ordinal   → ["Beginner", "Intermediate", "Advanced"]  
Interval  → [15°C, 20°C, 30°C]  
Ratio     → [10 kg, 20 kg, 40 kg]  
```

---

## 📂 Data Formats You’ll Encounter

* **CSV (Comma-Separated Values)** → Tables stored as text.
* **JSON (JavaScript Object Notation)** → Key-value pairs, great for APIs.
* **SQL Databases** → Structured queries with relational tables.
* **Parquet / ORC** → Columnar formats used in Big Data systems.

---

## 🌍 Real-World Examples

* **Retail**: CSV sales logs, customer info in SQL, product images as unstructured data.
* **Healthcare**: Patient records (structured), MRI scans (unstructured), HL7/JSON reports (semi-structured).
* **Social Media**: Tweets (text), engagement metrics (structured), profile metadata (semi-structured).

---

## 🎯 Why This Matters

Choosing the right tools depends on the type & format of your data:

* CSV → load with Pandas.
* JSON → parse into structured format.
* SQL → query directly.
* Unstructured (images/text) → needs specialized methods.

**👉 Next Step:** We’ll learn how to clean these different types of data so they’re ready for analysis.
