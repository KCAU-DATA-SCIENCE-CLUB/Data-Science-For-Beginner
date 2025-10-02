
# 📘 Lesson 2: Probability in Real Life

Probability helps us **measure uncertainty** and make **better decisions**. In data science, it’s the foundation of predictions — from recommending movies to detecting fraud.

---

## 🎲 What is Probability?

Probability is the **likelihood of an event occurring**, expressed as a number between `0` and `1`.

* `0` → Impossible event
* `1` → Certain event
* Example: Tossing a coin → Probability of heads = `0.5`

---

## 🧩 Real-Life Analogy

Think of probability as **"how confident you are about something happening."**

* Coin toss → 50% chance of heads
* Rolling a dice → 1/6 chance of rolling a 4
* Customer buying a product → 20% chance based on past data

---

## 📊 Formula for Probability

[
P(E) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}
]

Example: Rolling a dice and getting an even number
[
P(\text{Even}) = \frac{3}{6} = 0.5
]

---

## 🎥 Example in Data Science

* **Recommender Systems:** Netflix shows you a movie because there’s a **high probability** you’ll like it based on your history.
* **Spam Filtering:** Emails are classified as spam if the probability is above a threshold (say 0.9).

---

## 💡 Types of Probability

1. **Theoretical Probability** → Coin toss = 50%
2. **Experimental Probability** → Out of 100 tosses, 48 are heads → Probability = 0.48
3. **Conditional Probability** → Probability of event A given event B has occurred.

   * Example: Probability of a student passing **given** they studied for 10 hours.

---

## 📊 Visual Example

**Coin Toss Tree Diagram**

```
Start
 ├── Heads (0.5)
 └── Tails (0.5)
```

**Two Tosses Example:**

```
Start
 ├── H (0.5)
 │    ├── H (0.25) → HH
 │    └── T (0.25) → HT
 └── T (0.5)
      ├── H (0.25) → TH
      └── T (0.25) → TT
```

* Probability of getting **2 Heads** = 0.25

---

## 🔑 Key Takeaways

* Probability quantifies uncertainty.
* Real-life applications: recommender systems, spam detection, fraud detection.
* Conditional probability is crucial for understanding **dependencies**.

✅ Next, we’ll study **Distributions & Sampling** → the shapes probability can take in real-world data.
