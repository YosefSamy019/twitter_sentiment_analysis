# 🧠 Twitter Entity Sentiment Classification

This project performs **text classification** to identify **sentiment** (Positive/Negative) from Twitter text using classical ML models. It involves data preprocessing, TF-IDF text representation, training multiple models, and performance evaluation with visualizations.

---

## 📚 1. Libraries Import

```python
# Text Processing
import spacy, re
from textblob import TextBlob

# Data Handling
import numpy as np, pandas as pd

# Visualization
import matplotlib.pyplot as plt, seaborn as sns

# Custom Modules
from video.show_video import show_video
from video.video_maker import VideoMaker
from load_bar import LoadBarWithAutoIncrement, LoadBarReset
from object.object_cache import saveObject
import kagglehub

# ML
from sklearn.feature_extraction.text import TfidfVectorizer
```

---

## 📥 2. Dataset Import

* Data is downloaded using `kagglehub` from the **"twitter-entity-sentiment-analysis"** dataset.
* The data is read from two files and concatenated into one DataFrame.
* Only the relevant columns (target, sentence) are retained.

---

## 📊 3. Data Exploration

* View shape, column info, sample rows.
* Check and remove null values.

---

## 🧹 4. Data Cleaning

Multiple cleaning functions are applied sequentially:

1. **`cleanSentence()`**

   * Remove non-alphabet characters
   * Convert to lowercase

2. **`cleanSpaces()`**

   * Replace multiple spaces with a single space

3. **`normalizeSentence()`**

   * Lemmatize using SpaCy

4. **`removeStopWord()`**

   * Remove common stopwords

5. **`removeSingleChar()`**

   * Eliminate single-character tokens

6. *(Optional)* **`spellCorrect()`**

   * Correct spelling using TextBlob (commented due to speed)

Afterward:

* Remove empty strings
* Remove duplicates

---

## 📈 5. Dataset Visualization

* Plot target sentiment distribution using `sns.countplot`
* Plot sentence length distribution by class using `sns.kdeplot`
* Count unique words

---

## 🔡 6. Text Representation: TF-IDF

* Use **`TfidfVectorizer`** with **ngram range (1,3)** and top 10% of features.
* Convert sentences into sparse vector form.
* Save the TF-IDF vectorizer using `saveObject`.

Resulting dataset is saved to **`clean_dataset.csv`**.

---

## 🔁 7. ML Classification Models

### ➤ Dataset Preparation

* Reload cleaned dataset
* Filter for `Positive` and `Negative` classes only
* Encode labels using `LabelEncoder`
* Split into **train/test** (70/30 split)

### ➤ Models Trained:

* `LogisticRegression`
* `DecisionTreeClassifier`
* `RandomForestClassifier`
* `SVC (linear)`
* `MultinomialNB`, `GaussianNB`, `BernoulliNB`
* `KNeighborsClassifier`

Each model is:

* Trained and cached using `object_cache`
* Reloaded from cache if previously trained

---

## 📊 8. Evaluation

Each model is evaluated on:

* **Training and Testing accuracy**
* **Recall, Precision, and F1-score**

### Visualizations:

* Bar plots comparing all models across metrics
* Sorted table of test F1-scores

### Sample Output:

```bash
Best Model (Test F1):
RandomForestClassifier - F1: 0.89
```

---

## 💾 9. Saving Results

* All evaluations are saved to **`evaluation_dataset.csv`** for reproducibility.

---

## ✅ Summary

| Step                  | Description                            |
| --------------------- | -------------------------------------- |
| ✅ Load & explore data | Twitter sentiment data from Kaggle     |
| 🧹 Clean              | Regex, lemmatization, stopword removal |
| 🔠 TF-IDF             | Convert to numerical representation    |
| 🤖 ML Models          | 8 different classifiers tested         |
| 📊 Evaluation         | Metrics + Visualization                |
| 💾 Saved Assets       | TF-IDF vectorizer + CSVs + Models      |

---

## 📌 Notes

* Use `spellCorrect()` cautiously; it is **slow**.
* You can easily plug this into a **Streamlit** or **Flask** UI for user input and live prediction.

---