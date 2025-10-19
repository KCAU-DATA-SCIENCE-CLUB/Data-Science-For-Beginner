
# 🧭 Lesson 3: Classification — Making Categorical Predictions

> *“If regression predicts **how much**, classification predicts **which one**.”*

Classification is the heart of many real-world machine learning applications — from spam filters to medical diagnoses.
It’s about **assigning items to categories** based on their characteristics.

---

## 🧠 What is Classification?

Classification helps us predict **discrete labels** instead of continuous values.
For example:

* Email → *spam* or *not spam*
* Transaction → *fraudulent* or *legit*
* Passenger → *survived* or *did not survive*

---

## 🧩 Regression vs Classification

| Feature      | Regression           | Classification                           |
| ------------ | -------------------- | ---------------------------------------- |
| Output Type  | Continuous (numbers) | Categorical (labels)                     |
| Example      | Predict price        | Predict survival                         |
| Algorithm    | Linear Regression    | Logistic Regression, Decision Tree, etc. |
| Output Value | Real number          | Class probability                        |

---

## 🎯 Example: Predicting Titanic Survival

Let’s use the famous **Titanic dataset** — each passenger has attributes like:

| Feature         | Example            |
| --------------- | ------------------ |
| Age             | 29                 |
| Sex             | female             |
| Passenger Class | 1                  |
| Fare            | 75                 |
| Survived        | 1 *(target label)* |

Our goal:
Predict whether a passenger **survived (1)** or **did not survive (0)** based on their features.

---

## ⚙️ Building a Simple Classification Model

We’ll use **Logistic Regression** — a common algorithm for binary classification.

```python
# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Sample dataset (simplified)
data = {
    "age": [22, 38, 26, 35, 28, 42, 19, 50],
    "fare": [7.25, 71.28, 7.92, 53.10, 8.05, 13.00, 7.50, 30.00],
    "pclass": [3, 1, 3, 1, 3, 2, 3, 1],
    "survived": [0, 1, 1, 1, 0, 0, 1, 1]
}
df = pd.DataFrame(data)

# Features and target
X = df[["age", "fare", "pclass"]]
y = df["survived"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
preds = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, preds))
print("Confusion Matrix:\n", confusion_matrix(y_test, preds))
print("Report:\n", classification_report(y_test, preds))
```

---

## 📊 Visual: Logistic Regression Curve

When you plot logistic regression, the **S-shaped curve** shows probability:

```
   Probability
   1.0 |                      -----
       |                    /
       |                 /
       |              /
       |           /
       |________/________________
                  Feature value
```

Above 0.5 → class 1
Below 0.5 → class 0

---

## 📈 Confusion Matrix Explained

A confusion matrix tells you how well your model is performing:

|               | Predicted: 0        | Predicted: 1        |
| ------------- | ------------------- | ------------------- |
| **Actual: 0** | True Negative (TN)  | False Positive (FP) |
| **Actual: 1** | False Negative (FN) | True Positive (TP)  |

Accuracy = (TP + TN) / (TP + TN + FP + FN)

---

## ⚙️ Common Classification Algorithms

| Algorithm                        | Description                           | Example Use             |
| -------------------------------- | ------------------------------------- | ----------------------- |
| **Logistic Regression**          | Linear classifier for binary problems | Spam or Not Spam        |
| **Decision Tree**                | Splits data using rules               | Loan approval           |
| **Random Forest**                | Group of trees voting                 | Fraud detection         |
| **KNN (K-Nearest Neighbors)**    | Looks at nearby data points           | Handwriting recognition |
| **Naive Bayes**                  | Based on probabilities                | Sentiment analysis      |
| **SVM (Support Vector Machine)** | Finds best separating boundary        | Image classification    |

---

## 🎨 Visual Diagram: Classification Workflow

```
        🧮 Input Data
          ↓
  Feature Extraction
          ↓
   Model Learns Patterns
          ↓
   ┌──────────────┐
   │ Predict Class │
   └──────────────┘
          ↓
     📊 Output Labels
```

---

## 🧠 Real-World Examples of Classification

| Industry         | Example               | Description                    |
| ---------------- | --------------------- | ------------------------------ |
| 📧 Email         | Spam Detection        | Classify emails as spam or not |
| 💳 Banking       | Fraud Detection       | Flag suspicious transactions   |
| 🩺 Healthcare    | Disease Prediction    | Diagnose based on symptoms     |
| 🎵 Entertainment | Music Recommendation  | Group songs by mood            |
| 🛒 E-commerce    | Customer Segmentation | Target marketing by user type  |

---

## 🧩 Key Takeaways

* Classification predicts **categories**, not numbers.
* Logistic regression is the simplest way to start.
* Always analyze your confusion matrix — it tells the full story.
* Probabilities matter: output confidence is often more useful than a simple “yes/no.”


﻿
