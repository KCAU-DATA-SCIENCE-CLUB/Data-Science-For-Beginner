# 📘 Lesson 1: Types of Data & Real-World Examples

Data is everywhere — in apps, schools, hospitals, banks, even in the sports you watch. But not all data looks the same. Some is neat like a spreadsheet, some looks like messy text, and some is as complex as a video.

Think of data as **different types of books in a library**:

* 📄 **Structured Data** = neatly organized textbooks.
* 🌐 **Semi-structured Data** = magazines with tags & sections.
* 🎨 **Unstructured Data** = novels, poems, images, videos.

---

## 1. **Structured Data**

**Definition:** Organized in rows and columns, easy to store in databases.
**Story:** Like a library catalog — every book has an ID, title, and author.

**Examples:**

* Student grades in a school system.
* Bank transactions (date, amount, account number).
* Sports statistics tables.

**Visual:**

```
| StudentID | Name     | Grade |
|-----------|----------|-------|
| 101       | Alice    | A     |
| 102       | Bob      | B+    |
```

---

## 2. **Semi-structured Data**

**Definition:** Has structure but not as strict as tables. Uses tags, keys, and hierarchies.
**Story:** Like a magazine with sections, but not every magazine follows the same template.

**Examples:**

* JSON files (e.g., from APIs).
* XML documents.
* Tweets (text + hashtags + metadata).

**Visual (JSON):**

```json
{
  "student": {
    "id": 101,
    "name": "Alice",
    "grade": "A"
  }
}
```

---

## 3. **Unstructured Data**

**Definition:** Data without a fixed format, harder to organize but very common.
**Story:** Like a pile of novels, movies, or paintings — rich but not neatly organized.

**Examples:**

* Images (jpg, png).
* Videos (mp4, YouTube).
* Free text (reviews, essays, comments).

**Visual:**
🖼️ An image of a cat, 🎥 a 10-second video, or a 🌍 paragraph of raw text.

---

## 4. **Key Takeaway**

Different data types require different tools:

* 🗂️ **Structured** → Excel, SQL, Pandas.
* 🌐 **Semi-structured** → APIs, JSON libraries, Pandas.
* 🎨 **Unstructured** → NLP for text, CV for images, video analysis.

**Diagram (Flow):**

```
Data Sources
   ├── Structured → Tables → SQL/Pandas
   ├── Semi-structured → JSON/XML → APIs
   └── Unstructured → Text/Images/Video → NLP/CV
```

---

✅ Next Step: In the notebook (`notebook.ipynb`), we’ll **load and explore** one file of each type (CSV, JSON, text).
﻿
