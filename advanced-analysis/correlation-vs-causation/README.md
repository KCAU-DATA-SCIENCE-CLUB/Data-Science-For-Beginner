

# 🎯 **Lesson 1: Advanced Pandas — Grouping, Joining, and Feature Engineering**

When you reach this stage in data analysis, your goal shifts from *“understanding data”* to *“creating insight.”*
That’s where **advanced Pandas operations** come in — grouping, merging, and engineering new features that bring out deeper stories from your dataset.

---

## 🧠 Why This Matters

Data analysis is powerful not because of the tools — but because of the **questions you can now answer**:

* Which country has the highest CO₂ emissions per person?
* Which Netflix genre keeps viewers most engaged?
* Which team improved the most this season?

To answer these, you’ll need **grouping**, **joining**, and **feature creation**.

---

## 🧩 1. Grouping Data (`groupby`)

Grouping helps you **summarize** your data based on one or more categories.
Think of it like putting your data into “buckets” and then calculating insights within each bucket.

```python
import pandas as pd

df = pd.DataFrame({
    'Country': ['Kenya', 'Kenya', 'USA', 'USA', 'India', 'India'],
    'Year': [2020, 2021, 2020, 2021, 2020, 2021],
    'CO2_Emissions': [40, 42, 200, 210, 150, 155]
})

grouped = df.groupby('Country')['CO2_Emissions'].mean()
print(grouped)
```

**Output:**

```
Country
India    152.5
Kenya     41.0
USA      205.0
```

### 📊 Visual: Grouping

```
┌────────────┬───────────────┬────────────┐
│  Country   │  Year         │ Emissions  │
├────────────┼───────────────┼────────────┤
│  Kenya     │ 2020          │ 40         │
│  Kenya     │ 2021          │ 42         │
│  USA       │ 2020          │ 200        │
│  USA       │ 2021          │ 210        │
└────────────┴───────────────┴────────────┘
       ↓ groupby('Country')
┌────────────┬───────────────┐
│  Country   │ Avg Emission  │
├────────────┼───────────────┤
│  Kenya     │ 41.0          │
│  USA       │ 205.0         │
└────────────┴───────────────┘
```

---

## 🔗 2. Joining / Merging Datasets

When data is split across multiple sources — say, one file for population and another for CO₂ emissions — you need to **merge** them.

```python
pop = pd.DataFrame({'Country': ['Kenya', 'USA', 'India'], 'Population': [54, 330, 1390]})
merged = pd.merge(df, pop, on='Country', how='left')
print(merged.head())
```

**Output:**

```
Country  Year  CO2_Emissions  Population
Kenya    2020        40            54
...
```

### 🔄 Visual: Merge

```
[CO2 Data]        [Population Data]
 Country | CO2     Country | Population
----------         --------------------
 Kenya   | 40       Kenya   | 54
 USA     | 200      USA     | 330
 India   | 150      India   | 1390
          ↓ merge on Country
[Unified Table]
 Country | CO2 | Population
 Kenya   | 40  | 54
 USA     | 200 | 330
 India   | 150 | 1390
```

---

## 🧮 3. Feature Engineering

**Feature Engineering** means creating **new variables** that reveal insights.
For example, CO₂ per person = Total CO₂ / Population.

```python
merged['CO2_per_Capita'] = merged['CO2_Emissions'] / merged['Population']
print(merged[['Country', 'CO2_per_Capita']])
```

**Output:**

```
Country  CO2_per_Capita
Kenya        0.74
USA          0.61
India        0.11
```

This gives a fairer comparison between countries of different sizes.

---

## 💡 Real-World Applications

| Area            | Use Case                                    |
| --------------- | ------------------------------------------- |
| **Business**    | Calculate average customer spend per region |
| **Environment** | Analyze emissions per capita by country     |
| **Sports**      | Derive player efficiency = points/minute    |
| **Streaming**   | Compare watch hours per subscriber          |

---

## 🧭 Visual Summary

```
Raw Data → Group → Merge → Engineer → Insight
```

Each arrow represents a transformation that brings data closer to a story.

---

## 🚀 Next Lesson: Visualization with Purpose

