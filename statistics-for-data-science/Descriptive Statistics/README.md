
# 📊 Lesson 1: Descriptive Statistics

## 📖 Story

Imagine you’re a **teacher** with 30 students.
You give them a math test and now you’re holding a stack of scores.
Some scored very high, some very low — but you want a **summary** to quickly understand:

* How did the class do overall? 🤔
* Who is an outlier?
* Are scores spread out or very close?

That’s where **descriptive statistics** come in: they **summarize data** into numbers that are easier to interpret than raw lists.

---

## ✨ Key Concepts

| Concept                  | What it means                   | Example (test scores)              |
| ------------------------ | ------------------------------- | ---------------------------------- |
| **Mean (Average)**       | Sum of values ÷ count           | Average score = 75                 |
| **Median**               | Middle value when sorted        | Median score = 78                  |
| **Mode**                 | Most common value               | Mode = 80 (appears most often)     |
| **Variance / Std. Dev.** | How spread out the data is      | Std. dev. = 10 (scores vary a lot) |
| **Correlation**          | How two variables move together | Study hours ↑ → Exam score ↑       |

---

## 🛠 Example with Python

```python
import pandas as pd

# Example dataset: student exam scores
data = {
    "student": ["A","B","C","D","E","F","G","H","I","J"],
    "study_hours": [2, 3, 4, 5, 6, 8, 2, 9, 10, 7],
    "exam_score": [50, 55, 60, 65, 70, 85, 52, 90, 95, 80]
}

df = pd.DataFrame(data)
print(df)

# Mean, Median, Mode
print("Mean score:", df["exam_score"].mean())
print("Median score:", df["exam_score"].median())
print("Mode score:", df["exam_score"].mode()[0])

# Standard Deviation (spread of data)
print("Std Dev:", df["exam_score"].std())

# Correlation between study hours & exam scores
print(df.corr())
```

---

## 📈 Visuals

### 1. Distribution of Scores (Histogram)

Shows how many students scored in each range.

```
Exam Score Distribution
|      ***
|     *****
|    *******
|___|___|___|___|___
 50  60  70  80  90
```

### 2. Correlation (Scatter Plot)

* X-axis = Study Hours
* Y-axis = Exam Score

Students who studied more generally scored higher → **positive correlation** 📈.

---

## 💡 Why it Matters

Descriptive statistics are the **first step of analysis**:

* They give a **quick snapshot** of the data.
* Help spot **patterns** and **outliers**.
* Form the **foundation** for deeper techniques (probability, hypothesis testing, ML).

---

✅ Next Lesson: **Probability in Real Life** 🎲

---

Do you want me to **immediately continue with Lesson 2 (Probability)** in the same detailed style?

- Familiarity with data types and structures

## Getting Started

Open the `notebook.ipynb` file to begin learning about descriptive statistics and their applications in data analysis.
