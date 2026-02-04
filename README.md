# 🔍 Sentiment Analysis Web App (Flask + ML)

A production-ready **Sentiment Analysis web application** built using **Python, Machine Learning, and Flask**, deployed on **AWS EC2**.  
The app classifies customer reviews as **Positive or Negative** in real time.

---

## 🚀 Project Overview

This project analyzes real-world e-commerce reviews to understand customer sentiment and identify pain points from negative feedback.  
It includes **data preprocessing, model training, evaluation, and deployment** as a complete end-to-end ML system.

---

## 🎯 Objective

- Classify customer reviews into **Positive / Negative**
- Understand patterns behind negative sentiment
- Deploy an ML model as a **live web application**

---

## 📊 Dataset

- **Source:** Flipkart Product Reviews  
- **Product:** YONEX MAVIS 350 Nylon Shuttle  
- **Total Reviews:** 8,500+  
- **Features include:**
  - Review Text
  - Rating
  - Review Title
  - Review Date
  - Upvotes / Downvotes
  - Location


---

## 🧠 ML Workflow

### 1️⃣ Data Preprocessing
- Text cleaning (lowercasing, punctuation removal)
- Stopword removal
- Lemmatization
- Handling missing values
- Sentiment labeling based on ratings

### 2️⃣ Feature Engineering
- TF-IDF Vectorization
- N-gram representation
- Vocabulary size tuning

### 3️⃣ Model Training & Evaluation
Trained and compared multiple models:
- Naive Bayes
- Logistic Regression
- Decision Tree
- Random Forest
- SVM

📌 **Best Model:** Multinomial Naive Bayes  
📌 **Evaluation Metric:** F1-Score (Weighted)

---

## 🌐 Web Application

### Tech Stack
- **Backend:** Flask
- **ML Model:** Scikit-learn
- **Deployment:** AWS EC2 (Linux)
- **Server:** Flask

### Features
- Real-time sentiment prediction
- Clean and responsive UI
- Hosted on a public EC2 instance
- Background process management

---

## 🧩 Deployment Highlights

- Model & preprocessing consistency ensured (no training-serving skew)
- EC2 security groups configured for public access

---

## 🔗 Live Demo
👉 **http://54.163.218.199:5000/**

---

## 🛠 How to Run Locally

```bash
git clone https://github.com/mayurks23/sentiment-analysis-flask.git
cd sentiment-analysis-flask
pip install -r requirements.txt
python app.py
````

---

## 📌 Key Learnings

* End-to-end ML pipeline design
* Avoiding training-serving skew
* Deploying ML models to cloud infrastructure
* Monitoring live applications
* Real-world debugging & version compatibility handling

---

## 👤 Author

**Mayur Kumar Sourav**

* LinkedIn: [https://linkedin.com/in/your-profile](https://linkedin.com/in/mayur-kumar-sourav)
* GitHub: [https://github.com/your-username](https://github.com/mayurks23)


