"# potential-couscous" 
"# potential-couscous" 

# 📊 Customer Churn Prediction

A machine learning model to predict customer churn using historical customer data. This project helps businesses identify customers likely to leave and take proactive retention steps.

---

## 🧠 ML Model

- **Algorithm:** Random Forest Classifier  
- **Imbalance Handling:** SMOTE (Synthetic Minority Oversampling Technique)  
- **Accuracy:** ~87% (Update with your actual result)

---

## 📁 Features Used (19 total)

Examples:
- `tenure`, `MonthlyCharges`, `TotalCharges`, `Contract`, `PaymentMethod`, `InternetService`, etc.

> ✅ Custom feature engineering and label encoding applied.

---

## 📈 Performance Metrics

- Accuracy  
- Precision  
- Recall  
- F1 Score  
- Confusion Matrix

> Visualized using Seaborn/Matplotlib

---

## 🧪 EDA (Exploratory Data Analysis)

- Churn distribution analysis  
- Correlation heatmap  
- Feature impact plots (e.g., `Contract` vs. Churn)

---

## 🚀 Tech Stack

- **Language:** Python  
- **Libraries:**  
  `pandas`, `numpy`, `matplotlib`, `seaborn`, `sklearn`, `imblearn`, `pickle`

---

## 🖥️ Deployment

This project is ready for deployment using **Streamlit** for an interactive web interface.

> 🟢 You can input user details and predict churn live!

---

## 💡 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/Divyanshu-spec-code/potential-couscous.git
cd potential-couscous

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app (if available)
streamlit run app.py
