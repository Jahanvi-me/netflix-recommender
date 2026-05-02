# 🎬 Netflix AI Recommender System

A **content-based movie recommendation system** built using Machine Learning, with an interactive web app powered by Streamlit.

---

## 🚀 Project Overview

This project analyzes Netflix content and builds a recommendation system that suggests similar movies based on:

* 🎭 Genres
* 📝 Description
* 👥 Cast

The system uses **TF-IDF vectorization** and **cosine similarity** to find movies with similar content.

---

## 🧠 Key Features

* 🎯 Content-based movie recommendations
* 📊 Exploratory Data Analysis (EDA)
* ⚡ Fast similarity computation using TF-IDF
* 🌐 Interactive Streamlit web app
* 🔒 Designed for future AI-based explanations

---

## 📂 Project Structure

```text
Netflix_project/
│── app.py
│── README.md
│── requirements.txt
│
├── data/
│   ├── titles.csv
│   ├── credits.csv
│
├── notebooks/
│   └── Netflix_analysis.ipynb
```

---

## 📊 Exploratory Data Analysis

Detailed analysis is available in:

📁 `notebooks/Netflix_analysis.ipynb`

### Insights discovered:

* 🎭 Drama and Comedy dominate Netflix content
* 📈 Content production has grown rapidly over time
* ⭐ Most ratings fall between 6–8
* 🌍 USA leads content production globally

---

## ⚙️ How It Works

### 1️⃣ Data Processing

* Merge titles and credits datasets
* Clean missing values
* Extract relevant features

---

### 2️⃣ Feature Engineering

* Combine:

  * genres
  * description
  * cast
* Create a unified text representation

---

### 3️⃣ Vectorization

* Convert text into numerical format using **TF-IDF**
* Assign higher importance to unique words

---

### 4️⃣ Similarity Computation

* Use **cosine similarity** to measure similarity between movies

---

### 5️⃣ Recommendation

* Given a movie → find top similar movies
* Filter by same content type (Movie/TV Show)

---

## 🖥️ Running the App Locally

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run app

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

https://netflix-recommendation-app.streamlit.app

---

## 🌐 Deployment

This app can be deployed easily using **Streamlit Cloud**.

---

## 📸 Preview

![App Preview](<img width="953" height="794" alt="app_preview png" src="https://github.com/user-attachments/assets/425b2ced-4c64-48b7-ba61-8b8eaafb8d90" />)
![EDA_Preview](<img width="618" height="562" alt="eda_genre png" src="https://github.com/user-attachments/assets/e276c90a-0776-45ee-bc1c-f2ff01592574" />)
![EDA_Trends](<img width="598" height="475" alt="eda_trend png" src="https://github.com/user-attachments/assets/4bd12d41-9b42-465f-bbaa-65448e7e949b" />)





## 🔮 Future Improvements

* 🤖 AI-based explanation system (OpenAI integration)
* 🎬 Movie posters and visuals
* 🔍 Search-based input instead of dropdown
* ⭐ Personalized recommendations

---

## 👩‍💻 Author

Jahanvi Sania
GitHub Profile - https://github.com/Jahanvi-me

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
