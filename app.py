import streamlit as st
import pickle

# ==================================================
# Page Configuration
# ==================================================
st.set_page_config(
    page_title="AI Diagnosis Prediction System",
    page_icon="⚕️",
    layout="centered"
)

# ==================================================
# Hide Streamlit Default UI
# ==================================================
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ==================================================
# Background Styling
# ==================================================
background_image_url = "https://www.shutterstock.com/image-photo/hand-touching-modern-interface-digital-600nw-1927651358.jpg"

st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url({background_image_url});
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: absolute;
    inset: 0;
    background-color: rgba(0,0,0,0.75);
}}
</style>
""", unsafe_allow_html=True)

# ==================================================
# Hero Section
# ==================================================
st.title("AI Diagnosis Prediction System")
st.markdown("""
**An AI-powered decision support system demonstrating how machine learning models can assist
in disease risk estimation using structured health parameters.**
""")
st.markdown("---")

# ==================================================
# Top Tabs
# ==================================================
tab_predict, tab_about = st.tabs(
    ["🩺 Disease Prediction", "📊 About the System"]
)

# ==================================================
# Load Models (SAFE & CONSISTENT KEYS)
# ==================================================
models = {
    "diabetes": pickle.load(open("MODELS/diabetes_model.sav", "rb")),
    "heart": pickle.load(open("MODELS/heart_disease_model.sav", "rb")),
    "parkinsons": pickle.load(open("MODELS/parkinsons_model.sav", "rb")),
    "lungs": pickle.load(open("MODELS/lungs_disease_model.sav", "rb")),
    "thyroid": pickle.load(open("MODELS/Thyroid_model.sav", "rb")),
}

# ==================================================
# Input Helper
# ==================================================
def display_input(label, tooltip, key):
    return st.number_input(label, help=tooltip, key=key)

# ==================================================
# TAB 1 — DISEASE PREDICTION
# ==================================================
with tab_predict:

    st.subheader("How to Use")
    st.markdown("""
    1. Select a disease category  
    2. Enter clinical parameters  
    3. Click **Test Result** to view prediction  
    """)
    st.markdown("---")

    selected = st.selectbox(
        "Select Disease Category",
        [
            "Diabetes Prediction",
            "Heart Disease Prediction",
            "Parkinsons Prediction",
            "Lung Cancer Prediction",
            "Hypo-Thyroid Prediction",
        ],
    )

    # ---------------- Diabetes ----------------
    if selected == "Diabetes Prediction":
        st.subheader("Diabetes Prediction")

        Pregnancies = display_input("Pregnancies", "Number of pregnancies", "Pregnancies")
        Glucose = display_input("Glucose Level", "Plasma glucose concentration", "Glucose")
        BloodPressure = display_input("Blood Pressure", "Diastolic BP", "BP")
        SkinThickness = display_input("Skin Thickness", "Triceps skinfold", "Skin")
        Insulin = display_input("Insulin", "Serum insulin", "Insulin")
        BMI = display_input("BMI", "Body mass index", "BMI")
        DPF = display_input("Diabetes Pedigree Function", "Genetic likelihood", "DPF")
        Age = display_input("Age", "Age of patient", "Age")

        if st.button("Diabetes Test Result"):
            result = models["diabetes"].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age]])
            st.success("Diabetic" if result[0] == 1 else "Not Diabetic")

    # ---------------- Heart ----------------
    elif selected == "Heart Disease Prediction":
        st.subheader("Heart Disease Prediction")

        age = display_input("Age", "Age", "h_age")
        sex = display_input("Sex (1=Male, 0=Female)", "Gender", "h_sex")
        cp = display_input("Chest Pain Type", "0–3", "cp")
        trestbps = display_input("Resting BP", "Resting blood pressure", "bp")
        chol = display_input("Cholesterol", "Serum cholesterol", "chol")
        fbs = display_input("Fasting Blood Sugar", ">120 mg/dl", "fbs")
        restecg = display_input("ECG Result", "0–2", "ecg")
        thalach = display_input("Max Heart Rate", "Max achieved", "thalach")
        exang = display_input("Exercise Angina", "1=yes,0=no", "exang")
        oldpeak = display_input("ST Depression", "Induced by exercise", "oldpeak")
        slope = display_input("Slope", "0–2", "slope")
        ca = display_input("Major Vessels", "0–3", "ca")
        thal = display_input("Thalassemia", "0–2", "thal")

        if st.button("Heart Disease Test Result"):
            result = models["heart"].predict([[age, sex, cp, trestbps, chol, fbs, restecg,
                                               thalach, exang, oldpeak, slope, ca, thal]])
            st.success("Heart Disease Detected" if result[0] == 1 else "No Heart Disease")

    # ---------------- Parkinsons ----------------
    elif selected == "Parkinsons Prediction":
        st.subheader("Parkinson’s Disease Prediction")

        inputs = [display_input(f"Feature {i+1}", "Clinical voice measurement", f"p{i}") for i in range(22)]

        if st.button("Parkinson’s Test Result"):
            result = models["parkinsons"].predict([inputs])
            st.success("Parkinson’s Detected" if result[0] == 1 else "No Parkinson’s")

    # ---------------- Lung ----------------
    elif selected == "Lung Cancer Prediction":
        st.subheader("Lung Cancer Prediction")

        inputs = [display_input(f"Feature {i+1}", "Patient indicator", f"l{i}") for i in range(15)]

        if st.button("Lung Cancer Test Result"):
            result = models["lungs"].predict([inputs])
            st.success("Lung Cancer Detected" if result[0] == 1 else "No Lung Cancer")

    # ---------------- Thyroid ----------------
    elif selected == "Hypo-Thyroid Prediction":
        st.subheader("Hypo-Thyroid Prediction")

        age = display_input("Age", "Age", "t_age")
        sex = display_input("Sex (1=Male, 0=Female)", "Gender", "t_sex")
        on_thyroxine = display_input("On Thyroxine", "1=yes,0=no", "thy")
        tsh = display_input("TSH Level", "Hormone level", "tsh")
        t3_measured = display_input("T3 Measured", "1=yes,0=no", "t3m")
        t3 = display_input("T3 Level", "Hormone value", "t3")
        tt4 = display_input("TT4 Level", "Total thyroxine", "tt4")

        if st.button("Thyroid Test Result"):
            result = models["thyroid"].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
            st.success("Hypo-Thyroid Detected" if result[0] == 1 else "Normal Thyroid")

# ==================================================
# TAB 2 — ABOUT SYSTEM
# ==================================================
with tab_about:
    st.header("About the System")

    st.markdown("""
    ### What This System Does
    This application demonstrates how **trained machine learning models**
    can estimate disease risk using structured clinical inputs.

    ### Why This Matters
    - Shows real-world AI system design
    - Demonstrates ML model deployment
    - Bridges data science & product engineering

    ### How It Works
    1. User inputs health parameters  
    2. Pre-trained ML model processes data  
    3. System returns risk classification  

    ---
    ⚠️ **Disclaimer**  
    This system is for **educational purposes only** and must not be used
    for medical diagnosis or treatment decisions.
    """)
