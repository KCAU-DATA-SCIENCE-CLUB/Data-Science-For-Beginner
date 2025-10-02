# 🔍 Lesson 3: Data Exploration

Once data is cleaned, the next step is **exploration** — to **understand the story the data is telling**.
Think of it like being a **detective**: you’ve gathered clean notes, now you carefully examine them for **patterns, relationships, and clues**.

---

## 📖 Why Data Exploration Matters

Exploration helps us:

* See the **shape of the data** (ranges, distributions).
* Detect **trends, anomalies, and outliers**.
* Understand **relationships between variables**.
* Decide what analysis or models to try later.

Without exploration, we risk misinterpreting data or missing insights.

---

## 🛠️ Tools for Exploration

We’ll use:

* **Pandas**: quick stats (`.describe()`, `.value_counts()`, `.corr()`)
* **Matplotlib & Seaborn**: to **visualize patterns**
* **Pairplots & Heatmaps**: to check **relationships**

---

## 📊 Key Steps in Exploration

### 1. Summary Statistics

A quick snapshot of numeric data.

```python
import pandas as pd

df = pd.read_csv("data.csv")
df.describe()
```

👉 This shows **count, mean, std, min, max, quartiles**. It’s like a **health check** of your dataset.

---

### 2. Distribution of Variables

To see **how data is spread**.

**Histogram (distribution):**

```python
import matplotlib.pyplot as plt

df['age'].hist(bins=20)
plt.title("Distribution of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
```

📊 *Use this to spot skewed data or common ranges.*

**Boxplot (outliers):**

```python
import seaborn as sns

sns.boxplot(x=df['salary'])
plt.title("Salary Distribution")
plt.show()
```

👉 Boxplots help us detect **outliers** (values far outside normal range).

---

### 3. Exploring Categorical Variables

Count frequencies to see which categories dominate.

```python
df['gender'].value_counts()
```

**Visualized:**

```python
sns.countplot(x='gender', data=df)
plt.title("Gender Distribution")
plt.show()
```

👉 Helpful for checking **balance** in the dataset.

---

### 4. Relationships Between Variables

**Scatterplot (numeric vs numeric):**

```python
sns.scatterplot(x='age', y='salary', data=df)
plt.title("Age vs Salary")
plt.show()
```

👉 Use scatterplots to see **trends, clusters, or anomalies**.

**Correlation Matrix (linear relationships):**

```python
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```

📈 Correlations tell us if variables move together (positive, negative, or unrelated).

---

## 📌 Visual Examples

* Histogram (Distribution)
  ![histogram](https://upload.wikimedia.org/wikipedia/commons/3/3a/Histogram_example.png)

* Boxplot (Outlier Detection)
  ![boxplot](https://upload.wikimedia.org/wikipedia/commons/1/1a/Boxplot_vs_PDF.svg)

* Correlation Heatmap
  ![heatmap](https://seaborn.pydata.org/_images/seaborn-heatmap-2.png)

---

## ✅ Hands-On Notebook

In the notebook, you’ll:

* Run `.describe()` on a dataset.
* Plot histograms & boxplots for numeric columns.
* Use bar charts for categorical variables.
* Build scatterplots + heatmaps for relationships.

---

✨ By the end of this lesson, you’ll be able to **look at a new dataset and quickly “read its story”** before moving to advanced analysis.
﻿
