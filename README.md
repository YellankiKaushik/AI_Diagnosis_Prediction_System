# 🩺 AI Diagnosis Prediction System

An AI-powered decision support application that demonstrates how machine learning models
can estimate disease risk based on structured health parameters.

🔗 **Live Demo:**  
https://aidiagnose.streamlit.app/

---

## 📌 Project Overview

The **AI Diagnosis Prediction System** is a portfolio-grade machine learning application
designed to showcase end-to-end AI system development — from trained models to a
user-facing web interface.

The project focuses on **demonstration and learning**, highlighting how predictive models
can be deployed and interacted with in real time.

> ⚠️ This system is not intended for real medical diagnosis.

---

## 🎯 Why This Project?

Most machine learning projects stop at notebooks.

This project was built to:
- Demonstrate **AI system deployment**
- Bridge **ML models and UI**
- Showcase **real-world inference workflows**
- Serve as a **professional portfolio project**

---

## 🔄 How the System Works

1. User selects a disease category  
2. User enters relevant health parameters  
3. Inputs are passed to a pre-trained ML model  
4. The model performs inference  
5. Prediction result is displayed instantly  

Each disease uses an **independently trained model**.

---

## 🧠 Diseases Covered

- Diabetes Prediction  
- Heart Disease Prediction  
- Parkinson’s Disease Prediction  
- Lung Cancer Prediction  
- Hypo-Thyroid Prediction  

---

## 🤖 Machine Learning Models

The system uses supervised learning algorithms including:

- Logistic Regression  
- Support Vector Machines (SVM)  
- Tree-based classifiers  

Models are trained on domain-specific datasets and serialized
for fast runtime inference.

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **ML Libraries:** scikit-learn, numpy, pandas  
- **Web Framework:** Streamlit  
- **Deployment:** Streamlit Community Cloud  

---

## ▶️ Run Locally

```bash
# Clone the repository
git clone https://github.com/YellankiKaushik/AI_Diagnosis_Prediction_System.git

# Navigate to project directory
cd AI_Diagnosis_Prediction_System

# Create virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python -m streamlit run app.py
