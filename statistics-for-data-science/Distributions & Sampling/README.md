# 📘 Lesson 3: Distributions & Sampling

Probability gives us the foundation, but in the real world data doesn’t just sit as single probabilities — it **forms patterns**. These patterns are called **distributions**. Understanding them is essential in data science because they tell us how data behaves.

---

## 📊 What is a Distribution?

A **distribution** shows how values are spread across possible outcomes.

* Height of people → Most around average (bell curve).
* Dice roll → Equal probability for 1 to 6 (uniform).
* Customer purchases → Few spend a lot, most spend small (skewed).

📌 **Visual Aid:**

* Bell Curve diagram (Normal Distribution).
* Flat Bar for Uniform Distribution.
* Right-skewed curve for Income.

---

## 🎨 Common Distributions

### 1. Uniform Distribution

Every outcome has the same chance.

* Example: Rolling a fair dice.
* Graph: Flat line across values.
  📌 **Visual Aid:** Bar plot with equal heights.

### 2. Normal Distribution (Bell Curve)

Data clusters around the mean.

* Example: Heights, test scores.
* Symmetrical, with most values near the center.
  📌 **Visual Aid:** Bell curve with mean in center.

### 3. Skewed Distribution

One side has more values than the other.

* Example: Income → most people earn average, a few earn very high.
  📌 **Visual Aid:** Right-skewed histogram.

---

## 🎯 Sampling

We often cannot collect all possible data, so we use **sampling**.

* **Population** → Entire dataset (all students in a country).
* **Sample** → Subset (100 students surveyed).

Why sample?

* Saves time & cost.
* Helps estimate population behavior.

📌 **Visual Aid:** Diagram of a big circle (population) and a small selected circle inside it (sample).

---

## 🐍 Python Examples

### 1. Normal Distribution Simulation

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 samples from a normal distribution
data = np.random.normal(loc=50, scale=10, size=1000)

plt.hist(data, bins=30, density=True, alpha=0.6, color="skyblue")
plt.title("Normal Distribution (mean=50, sd=10)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

### 2. Uniform Distribution Simulation

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate uniform data between 0 and 1
data = np.random.uniform(0, 1, 1000)

plt.hist(data, bins=20, density=True, alpha=0.6, color="orange")
plt.title("Uniform Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

### 3. Sampling Example

```python
import numpy as np

# Population: 1 to 1000
population = np.arange(1, 1001)

# Take a sample of 50
sample = np.random.choice(population, size=50, replace=False)

print("Sample mean:", sample.mean())
print("Population mean:", population.mean())
```

---

## 🔑 Key Takeaways

* **Distributions** describe how data is spread.
* Normal, uniform, and skewed are common types.
* **Sampling** lets us estimate population characteristics efficiently.
* Visuals (curves, histograms, diagrams) help make patterns clear.
* Python brings these patterns to life with simulations.

✅ Next: **Lesson 4: Hypothesis Testing** → Making data-driven decisions.
