# 🔍 Lesson 4: Exploratory Data Analysis (EDA)

Once you have collected and cleaned your data, the next step is **exploring it**. Exploratory Data Analysis (EDA) helps you **discover patterns, spot anomalies, check assumptions, and form hypotheses** before doing deeper analysis or modeling.

Think of it like being a detective with a magnifying glass — you’re not solving the case yet, but you’re carefully examining every clue.

---

## 🎯 Goals of EDA

1. **Understand your dataset** → size, shape, data types.
2. **Summarize key statistics** → averages, medians, spread.
3. **Visualize distributions** → histograms, boxplots, scatterplots.
4. **Spot patterns & anomalies** → trends, correlations, missing values.
5. **Form early hypotheses** → “Could X be affecting Y?”

---

## 🛠️ Common EDA Steps

1. **Inspect the dataset**

   * `.head()`, `.info()`, `.describe()` in Pandas.

2. **Check missing values & duplicates**

   * `df.isnull().sum()`, `df.duplicated().sum()`.

3. **Explore single variables (Univariate Analysis)**

   * Histograms, bar charts, pie charts.

4. **Explore relationships (Bivariate/Multivariate Analysis)**

   * Scatterplots, correlation heatmaps, pair plots.

---

## 📊 Example

Imagine analyzing a dataset of **student grades**.

* Histogram → shows most students score between 60–80.
* Scatterplot (hours studied vs. grade) → shows positive relationship.
* Boxplot → highlights one outlier student who scored very low despite studying many hours.

---

## 🖼️ Visual Summary

```
Data → Summarize → Visualize → Spot Patterns → Hypothesize
```

(Like a detective gathering evidence before building a case.)

---

## 🌍 Real-World Applications

* **Business** → Explore customer purchase patterns.
* **Healthcare** → Spot unusual patient results early.
* **Sports** → Find hidden trends in player performance data.

---

## 🚀 Next Step

Once you understand your data through EDA, you’re ready to **move into data visualization**: lession 5
