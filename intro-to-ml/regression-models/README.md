
# 📈 Lesson 2: Regression — Predicting Continuous Values

> *“If data analysis explains the past, regression helps us forecast the future.”*

Regression is one of the **most important concepts** in Machine Learning.
It helps us **predict a continuous value** — like prices, scores, or temperatures — based on one or more input features.

---

## 🧠 What is Regression?

Regression finds a mathematical relationship between a **dependent variable (target)** and one or more **independent variables (features)**.

Think of it as drawing a **best-fit line** through your data to predict unknown values.

### 🎯 Example: Predicting House Prices

Imagine we have this dataset:

| 🏠 Size (sqft) | 🛏️ Bedrooms | 💰 Price ($) |
| -------------- | ------------ | ------------ |
| 1000           | 2            | 150,000      |
| 1500           | 3            | 200,000      |
| 2000           | 3            | 250,000      |
| 2500           | 4            | 300,000      |

We want to **predict price** based on **size** and **bedrooms**.

---

## 🧩 The Regression Equation

[
\text{Price} = m_1(\text{Size}) + m_2(\text{Bedrooms}) + c
]

Where:

* (m_1, m_2) = weights (the influence of each feature)
* (c) = intercept (base value)
* The model “learns” these weights from training data.

### 📊 Visual Explanation

```
      |
Price |          ●
      |      ●
      |   ●
      |●___________________
           Size (sqft)
```

The line represents the **model’s prediction** — a smooth relationship between size and price.

---

## ⚙️ Types of Regression

| Type                           | Description                  | Example                   |
| ------------------------------ | ---------------------------- | ------------------------- |
| **Linear Regression**          | Straight-line relationship   | Price vs. Size            |
| **Multiple Linear Regression** | More than one feature        | Price vs. Size + Bedrooms |
| **Polynomial Regression**      | Curved relationship          | Age vs. Salary            |
| **Logistic Regression**        | For binary outcomes (yes/no) | Survived vs. Died         |

---

## 🧰 Building a Simple Model with `scikit-learn`

Let’s predict house prices using **Linear Regression**:

```python
# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "size": [1000, 1500, 2000, 2500, 3000],
    "price": [150000, 200000, 250000, 300000, 350000]
}
df = pd.DataFrame(data)

# Split into features and target
X = df[["size"]]
y = df["price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
preds = model.predict(X_test)

# Plot
plt.scatter(X, y, color="blue")
plt.plot(X, model.predict(X), color="red")
plt.title("House Price Prediction")
plt.xlabel("Size (sqft)")
plt.ylabel("Price ($)")
plt.show()
```

---

## 📊 Interpreting Results

After training:

```python
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)
```

If:

```
Coefficient: [100]
Intercept: 50000
```

It means:
[
\text{Price} = 100 \times \text{Size} + 50000
]

So, for a 2000 sqft house:
[
\text{Price} = 100 \times 2000 + 50000 = 250000
]

---

## 🎨 Visual Diagram: Regression in Action

```
 Input Features  ───►  Model Learns Relationship  ───►  Predict Output
     (Size)                   (Best-fit Line)             (Price)
```

---

## 🧩 Evaluation Metrics

| Metric                        | Measures                    | Ideal Value |
| ----------------------------- | --------------------------- | ----------- |
| **MAE (Mean Absolute Error)** | Average absolute difference | Close to 0  |
| **MSE (Mean Squared Error)**  | Squared difference          | Close to 0  |
| **R² (R-squared)**            | Model accuracy (0–1)        | Close to 1  |

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("MAE:", mean_absolute_error(y_test, preds))
print("MSE:", mean_squared_error(y_test, preds))
print("R²:", r2_score(y_test, preds))
```

---

## 🌍 Real-World Examples of Regression

| Application    | What it Predicts | Impact                |
| -------------- | ---------------- | --------------------- |
| 📈 Finance     | Stock prices     | Investment strategies |
| 🏠 Real Estate | House prices     | Market valuation      |
| 🌡️ Weather    | Temperature      | Climate forecasting   |
| 🚗 Automotive  | Car resale value | Pricing tools         |

---

## 🧠 Key Takeaways

* Regression predicts **continuous** values.
* It learns relationships between **input features** and **target variables**.
* The **best-fit line** minimizes the distance between predictions and real values.
* It’s the **foundation of predictive modeling** in ML.

