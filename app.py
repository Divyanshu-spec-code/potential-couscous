import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
@st.cache_resource
def load_model():
    with open("churn_model_pipeline.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

st.set_page_config(page_title="Customer Churn Predictor", layout="wide")
st.title("📊 Customer Churn Prediction App")

# Select Mode
mode = st.radio("Choose Prediction Mode", ["🔘 Manual Input", "📁 CSV Upload"])

# ---------- MANUAL MODE ----------
if mode == "🔘 Manual Input":
    st.subheader("🧍 Manual Input Mode")

    if st.button("🔁 Load Demo Data"):
        demo_data = {
            'gender': 'Female',
            'SeniorCitizen': 0,
            'Partner': 'Yes',
            'Dependents': 'No',
            'tenure': 12,
            'PhoneService': 'Yes',
            'MultipleLines': 'No',
            'InternetService': 'Fiber optic',
            'OnlineSecurity': 'No',
            'OnlineBackup': 'Yes',
            'DeviceProtection': 'No',
            'TechSupport': 'No',
            'StreamingTV': 'Yes',
            'StreamingMovies': 'No',
            'Contract': 'Month-to-month',
            'PaperlessBilling': 'Yes',
            'PaymentMethod': 'Electronic check',
            'MonthlyCharges': 70.35,
            'TotalCharges': 1397.475
        }
    else:
        demo_data = {
            'gender': '',
            'SeniorCitizen': 0,
            'Partner': '',
            'Dependents': '',
            'tenure': '',
            'PhoneService': '',
            'MultipleLines': '',
            'InternetService': '',
            'OnlineSecurity': '',
            'OnlineBackup': '',
            'DeviceProtection': '',
            'TechSupport': '',
            'StreamingTV': '',
            'StreamingMovies': '',
            'Contract': '',
            'PaperlessBilling': '',
            'PaymentMethod': '',
            'MonthlyCharges': '',
            'TotalCharges': ''
        }

    input_data = {}
    for key, default in demo_data.items():
        if key in ['tenure', 'MonthlyCharges', 'TotalCharges']:
            val = st.text_input(f"{key} (numeric)", value=str(default))
            try:
                input_data[key] = float(val) if val.strip() != "" else np.nan
            except:
                input_data[key] = np.nan
        elif key == 'SeniorCitizen':
            input_data[key] = st.selectbox(key, [0, 1], index=default if default in [0, 1] else 0)
        else:
            input_data[key] = st.selectbox(key, options=["", "Yes", "No", "Male", "Female", "Month-to-month", "One year", "Two year",
                                                         "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)",
                                                         "DSL", "Fiber optic", "No internet service", "No phone service"],
                                           index=0 if default == "" else 1)

    if st.button("🚀 Predict"):
        try:
            df = pd.DataFrame([input_data])
            st.dataframe(df)
            prediction = model.predict(df)[0]
            st.success(f"📢 Prediction: {'Yes (Will Churn)' if prediction == 1 else 'No (Will Not Churn)'}")
        except Exception as e:
            st.error(f"❌ Error in prediction: {e}")


# ---------- CSV MODE ----------
elif mode == "📁 CSV Upload":
    st.subheader("📂 CSV Upload Mode")
    uploaded_file = st.file_uploader("Upload your raw customer CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)

            # Clean numeric columns
            numeric_cols = ['TotalCharges', 'MonthlyCharges', 'tenure']
            for col in numeric_cols:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

            st.write("✅ Uploaded Raw Data:")
            st.dataframe(df.head())

            # Predict
            predictions = model.predict(df)
            result_df = df.copy()
            result_df["Churn Prediction"] = ["Yes" if pred == 1 else "No" for pred in predictions]

            st.subheader("📈 Prediction Results")
            st.dataframe(result_df)

            # Download predictions
            csv_data = result_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Prediction Results as CSV",
                data=csv_data,
                file_name="churn_predictions.csv",
                mime="text/csv"
            )
        except Exception as e:
            st.error(f"❌ Error processing file: {e}")
    else:
        st.info("Upload a CSV file to predict churn for multiple customers.")
