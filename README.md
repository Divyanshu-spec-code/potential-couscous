"# potential-couscous" 
"# potential-couscous" 

 📊 Customer Churn Prediction App

This is a production-ready **Streamlit web application** that predicts whether a telecom
customer will churn or not using a trained **Random Forest Classifier**. It uses a full
preprocessing pipeline with **SMOTE** to handle class imbalance and supports both **manual
 input** and **bulk CSV upload**.

---

## 🔍 Features

- 🧍 **Manual Prediction Mode**: Input individual customer details via form.
- 📁 **CSV Upload Mode**: Upload a raw dataset and get predictions for multiple customers.
- 🧠 **Preprocessing Pipeline**: Handles missing values, categorical encoding, and numeric cleaning.
- 📥 **Download Predictions**: Output CSV with predicted churn labels.
- ✅ **Built With**: Python, Scikit-learn, Imbalanced-learn, Streamlit.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/customer-churn-app.git
cd customer-churn-app

### 2. Install Dependencied
pip install -r requirements.txt

### 3. Run the Streamlit app
streamlit run app.py
