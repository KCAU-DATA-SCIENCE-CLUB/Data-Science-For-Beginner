# 📘 Lesson 2: Cleaning Data

Raw data is rarely ready for analysis. It often comes messy — with missing values, duplicates, typos, and outliers.
Think of it as **a student’s rough notes that need to be rewritten into a neat report**.

If we don’t clean data, our analysis and models can be misleading.

---

## 1. **Why Cleaning Matters**

* 🧹 **Accuracy** → Errors in data = errors in results.
* 🔍 **Clarity** → Clean data is easier to explore.
* 🤖 **Readiness** → Machine learning models can’t handle messy input.

**Story:** Imagine cooking with spoiled ingredients — no matter how good the recipe, the meal will be bad. Data cleaning ensures our “ingredients” are fresh.

---

## 2. **Common Data Problems**

### a) Missing Values

* Example: A student’s grade is blank.
* Options: Drop the row, fill with mean/median, or predict missing values.

**Visual:**

```
| Student | Math | English |
|---------|------|---------|
| Alice   | 90   | 85      |
| Bob     |      | 78      |  ❌ Missing
```

---

### b) Duplicates

* Example: Same customer entered twice in a system.
* Solution: Drop duplicate rows.

**Visual:**

```
| ID | Name  | Purchase |
|----|-------|----------|
| 1  | John  | Shoes    |
| 1  | John  | Shoes    |  ❌ Duplicate
```

---

### c) Typos & Inconsistencies

* Example: "Kenya" vs "Kenia" vs "KE".
* Solution: Standardize formats.

---

### d) Outliers

* Example: A student has “999” as their test score.
* Solution: Check if it’s an error or a valid rare case.

---

## 3. **Tools & Functions in Pandas**

* `.isnull()` → find missing values
* `.fillna()` → replace missing values
* `.dropna()` → remove missing values
* `.drop_duplicates()` → remove duplicates
* `.replace()` → fix typos
* Statistical checks (`describe()`) → spot outliers

---

## 4. **Workflow Diagram**

```
Raw Data
   ↓
Detect Problems (missing, duplicates, typos, outliers)
   ↓
Choose Strategy (drop, fill, standardize)
   ↓
Clean Data ✅
```

---

## 5. **Mini Example**

**Messy Data:**

```
| Name  | Age | Country  |
|-------|-----|----------|
| Alice | 25  | Kenya    |
| Bob   |     | KE       |
| Bob   |     | KE       |
| Cara  | 999 | Kenia    |
```

**After Cleaning:**

```
| Name  | Age | Country |
|-------|-----|---------|
| Alice | 25  | Kenya   |
| Bob   | 24  | Kenya   |
| Cara  | 29  | Kenya   |
```

---

## ✅ Next Step

In the `notebook.ipynb`, we’ll:

* Load a messy dataset.
* Detect missing values, duplicates, and outliers.
* Apply Pandas cleaning functions step by step.
﻿
