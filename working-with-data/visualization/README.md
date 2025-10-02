# 📊 Lesson 3: Data Visualization with Matplotlib & Seaborn

Data is powerful, but raw numbers can be overwhelming. **Visualization transforms data into stories**—patterns, trends, and relationships that our eyes can easily understand. In this lesson, we’ll learn how to use **Matplotlib** and **Seaborn** to create clear, meaningful charts.

---

## 🔑 Why Visualization Matters

* **See patterns**: Spot trends that aren’t obvious in tables.
* **Communicate effectively**: Charts tell stories quickly.
* **Make decisions**: Visuals guide better business and research choices.

> *“A good visualization is like a window into the soul of the data.”*

---

## 🛠️ Tools: Matplotlib & Seaborn

* **Matplotlib** → the foundation (low-level, customizable).
* **Seaborn** → built on top of Matplotlib, easier & prettier.

---

## 📌 Basics with Matplotlib

### 1. Line Plot

```python
import matplotlib.pyplot as plt

# Sample data
years = [2018, 2019, 2020, 2021, 2022]
sales = [100, 120, 150, 130, 170]

plt.plot(years, sales, marker='o')
plt.title("Sales Over Years")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()
```

🔍 **What’s happening?**

* `plt.plot()` → draws the line.
* `marker='o'` → shows points.
* Labels + title → tell the story.

---

### 2. Bar Chart

```python
products = ['A', 'B', 'C']
revenue = [300, 450, 150]

plt.bar(products, revenue, color=['skyblue', 'orange', 'green'])
plt.title("Product Revenue")
plt.show()
```

---

## 📌 Basics with Seaborn

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Histogram
sns.histplot(tips["total_bill"], bins=20, kde=True)
plt.title("Distribution of Total Bills")
plt.show()

# Scatterplot
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
plt.title("Bill vs Tip by Time")
plt.show()
```

✨ Seaborn gives you **beautiful plots with less code**.

---

## 🎨 Visual Examples

* **Line plots** → trends over time.
* **Bar plots** → category comparisons.
* **Histograms** → distributions.
* **Scatterplots** → relationships.

*(Add diagrams of chart types in `assets/` folder.)*

---

## 🚀 Mini Challenge

Take the **World Happiness Dataset** and try:

1. Line chart → Happiness Score trend over years for 1 country.
2. Bar chart → Top 10 happiest countries in 2022.
3. Scatterplot → GDP per capita vs Happiness Score.

---

✅ **Key Takeaways**

* Use **Matplotlib** when you want full control.
* Use **Seaborn** when you want quick, clean visuals.
* Always add **labels, titles, legends** → they tell the story!

📂 Save charts into `/assets/lesson-3-viz-examples/`.
﻿
