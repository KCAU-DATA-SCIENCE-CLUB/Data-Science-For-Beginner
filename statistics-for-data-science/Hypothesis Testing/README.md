# 📘 Lesson 4: Hypothesis Testing

Data science is not just about describing or visualizing data — it’s about making **decisions with confidence**. Hypothesis testing helps us decide if a result is **real or just due to chance**.

---

## 🎯 What is a Hypothesis?

A **hypothesis** is a claim or assumption we test using data.

* **Null Hypothesis (H₀):** Default belief (nothing new happening).
* **Alternative Hypothesis (H₁):** The opposite claim (something is happening).

📌 Example:

* H₀: A new teaching method has **no effect** on student scores.
* H₁: The new teaching method **improves** student scores.

---

## 🔑 Key Concepts

1. **p-value**

   * Probability of observing the result (or more extreme) if H₀ is true.
   * Small p-value → evidence against H₀.

2. **Significance Level (α)**

   * Threshold (commonly 0.05).
   * If p-value < α → reject H₀.

3. **Type I & Type II Errors**

   * Type I: Rejecting H₀ when it’s true (false alarm).
   * Type II: Failing to reject H₀ when H₁ is true (missed detection).

📌 **Visual Aid:** Flowchart of decision-making (p-value < 0.05 → reject H₀, else fail to reject).

---

## 🧪 Example: Student Test Scores

Suppose we want to test if a new study technique improves scores.

* Group A (control): Old method → 70, 72, 68, 65, 74
* Group B (treatment): New method → 78, 82, 85, 80, 79

---

## 🐍 Python Example

### t-test for difference in means

```python
import numpy as np
from scipy import stats

# Scores
group_a = np.array([70, 72, 68, 65, 74])
group_b = np.array([78, 82, 85, 80, 79])

# t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)

print("t-statistic:", t_stat)
print("p-value:", p_value)

# Decision
alpha = 0.05
if p_value < alpha:
    print("Reject H₀ → New method improves scores!")
else:
    print("Fail to reject H₀ → No significant improvement.")
```

---

## 🎨 Visual Aid Ideas

* Overlapping histograms of Group A & B scores.
* Flowchart: Hypothesis → Test → Decision (Reject / Fail to Reject).
* Error illustration: Type I vs Type II.

---

## 🔑 Key Takeaways

* Hypothesis testing lets us **verify claims with data**.
* Always define H₀ and H₁ clearly.
* p-values and α guide decision-making.
* Mistakes (Type I & II) are always possible, so results need context.

✅ Next: **Mini Project — “Is student performance related to study hours?”**
We’ll apply descriptive statistics, probability, distributions, and hypothesis testing in one analysis.
