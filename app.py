import streamlit as st
import pandas as pd
import joblib
import warnings

from sklearn.preprocessing import LabelEncoder

# Suppress warnings
warnings.filterwarnings("ignore")

# Page configuration
st.set_page_config(page_title="Student Performance Prediction - Jaya Jaya Institute", layout="wide")
st.title("🎓 Student Performance Prediction - Jaya Jaya Institute")

# Load model and preprocessing files
MODEL_PATH = "best_model.pkl"
FEATURES_PATH = "selected_features.pkl"
SCALER_PATH = "scaler.pkl"

try:
    model = joblib.load(MODEL_PATH)
    selected_features = joblib.load(FEATURES_PATH)
    scaler = joblib.load(SCALER_PATH)
except Exception as e:
    st.error(f"❌ Failed to load model/preprocessing files: {e}")
    st.stop()

# File uploader
uploaded_file = st.file_uploader("📤 Upload your CSV file for prediction", type=["csv"])

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        st.success("✅ File successfully uploaded!")
        with st.expander("📋 Data Preview"):
            st.dataframe(data)
    except Exception as e:
        st.error(f"❌ Failed to read file: {e}")
        st.stop()

    # Label Encoding for categorical variables
    X_encoded = data.copy()
    categorical_cols = X_encoded.select_dtypes(include=["object"]).columns
    le = LabelEncoder()
    for col in categorical_cols:
        X_encoded[col] = le.fit_transform(X_encoded[col])

    # Validate feature columns
    missing_cols = set(selected_features) - set(X_encoded.columns)
    if missing_cols:
        st.warning(f"⚠️ The following columns are missing in your uploaded file: {missing_cols}")
        st.info("Please check your file format and upload again.")
        st.stop()

    # Select and transform features
    X_input = X_encoded[selected_features]
    X_scaled_np = scaler.transform(X_input)
    X_scaled_df = pd.DataFrame(X_scaled_np, columns=selected_features)

    # Prediction
    predictions = model.predict(X_scaled_df)
    prediction_df = pd.DataFrame(predictions, columns=["Prediction"])

    # Map prediction values
    prediction_mapping = {0: "Graduate", 1: "Dropout", 2: "Enrolled"}
    prediction_df["Prediction"] = prediction_df["Prediction"].map(prediction_mapping)

    # Combine results
    final_output = pd.concat([data.reset_index(drop=True), prediction_df], axis=1)

    st.success("✅ Prediction completed successfully!")
    st.dataframe(final_output)

    # Download result
    csv = final_output.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Prediction Results", csv, "prediction_results.csv", "text/csv")

else:
    st.info("⬆️ Please upload a CSV file to start the prediction process.")
