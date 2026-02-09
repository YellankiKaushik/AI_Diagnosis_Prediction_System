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
# Background Styling (Subtle, Professional)
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
    background-color: rgba(0,0,0,0.78);
}}
.section-card {{
    background-color: rgba(255,255,255,0.06);
    padding: 24px;
    border-radius: 14px;
    margin-bottom: 20px;
}}
</style>
""", unsafe_allow_html=True)

# ==================================================
# HERO SECTION (Clean & Minimal)
# ==================================================
st.title("AI Diagnosis Prediction System")
st.markdown(
    "A machine learning–based decision support system for **educational and demonstration purposes**."
)

st.markdown("---")

# ==================================================
# TOP TABS
# ==================================================
tab_predict, tab_about = st.tabs(
    ["🩺 Disease Prediction", "📊 About the System"]
)

# ==================================================
# LOAD MODELS
# ==================================================
models = {
    "diabetes": pickle.load(open("MODELS/diabetes_model.sav", "rb")),
    "heart": pickle.load(open("MODELS/heart_disease_model.sav", "rb")),
    "parkinsons": pickle.load(open("MODELS/parkinsons_model.sav", "rb")),
    "lungs": pickle.load(open("MODELS/lungs_disease_model.sav", "rb")),
    "thyroid": pickle.load(open("MODELS/Thyroid_model.sav", "rb")),
}

# ==================================================
# INPUT HELPER
# ==================================================
def display_input(label, tooltip, key):
    return st.number_input(label, help=tooltip, key=key)

# ==================================================
# TAB 1 — DISEASE PREDICTION
# ==================================================
with tab_predict:

    st.markdown(
        """
        <div class="section-card">
        <strong>How to use this system</strong><br><br>
        1. Select a disease category<br>
        2. Enter the required clinical parameters<br>
        3. Click <b>Test Result</b> to view the prediction
        </div>
        """,
        unsafe_allow_html=True,
    )

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

    col_inputs, col_result = st.columns([2, 1])

    # ---------------- DIABETES ----------------
    if selected == "Diabetes Prediction":

        with col_inputs:
            st.subheader("Input Parameters")

            Pregnancies = display_input("Pregnancies", "Number of pregnancies", "d1")
            Glucose = display_input("Glucose Level", "Plasma glucose concentration", "d2")
            BloodPressure = display_input("Blood Pressure", "Diastolic BP", "d3")
            SkinThickness = display_input("Skin Thickness", "Triceps skinfold", "d4")
            Insulin = display_input("Insulin", "Serum insulin", "d5")
            BMI = display_input("BMI", "Body mass index", "d6")
            DPF = display_input("Diabetes Pedigree Function", "Genetic likelihood", "d7")
            Age = display_input("Age", "Age of the patient", "d8")

            predict = st.button("Diabetes Test Result")

        with col_result:
            st.subheader("Prediction Result")

            if predict:
                result = models["diabetes"].predict([[Pregnancies, Glucose, BloodPressure,
                                                      SkinThickness, Insulin, BMI, DPF, Age]])
                st.success(
                    "Diabetic" if result[0] == 1 else "Not Diabetic"
                )

    # ---------------- HEART ----------------
    elif selected == "Heart Disease Prediction":

        with col_inputs:
            st.subheader("Input Parameters")

            age = display_input("Age", "Age", "h1")
            sex = display_input("Sex (1=Male, 0=Female)", "Gender", "h2")
            cp = display_input("Chest Pain Type", "0–3", "h3")
            trestbps = display_input("Resting BP", "Blood pressure", "h4")
            chol = display_input("Cholesterol", "Serum cholesterol", "h5")
            fbs = display_input("Fasting Blood Sugar", ">120 mg/dl", "h6")
            restecg = display_input("ECG Result", "0–2", "h7")
            thalach = display_input("Max Heart Rate", "Maximum rate", "h8")
            exang = display_input("Exercise Angina", "1=yes,0=no", "h9")
            oldpeak = display_input("ST Depression", "Exercise induced", "h10")
            slope = display_input("Slope", "0–2", "h11")
            ca = display_input("Major Vessels", "0–3", "h12")
            thal = display_input("Thalassemia", "0–2", "h13")

            predict = st.button("Heart Disease Test Result")

        with col_result:
            st.subheader("Prediction Result")

            if predict:
                result = models["heart"].predict([[age, sex, cp, trestbps, chol, fbs,
                                                   restecg, thalach, exang,
                                                   oldpeak, slope, ca, thal]])
                st.success(
                    "Heart Disease Detected" if result[0] == 1 else "No Heart Disease"
                )

    # ---------------- PARKINSONS ----------------
    elif selected == "Parkinsons Prediction":

        with col_inputs:
            st.subheader("Input Parameters")
            inputs = [
                display_input(f"Feature {i+1}", "Clinical voice parameter", f"p{i}")
                for i in range(22)
            ]
            predict = st.button("Parkinson’s Test Result")

        with col_result:
            st.subheader("Prediction Result")
            if predict:
                result = models["parkinsons"].predict([inputs])
                st.success(
                    "Parkinson’s Detected" if result[0] == 1 else "No Parkinson’s"
                )

    # ---------------- LUNG ----------------
    elif selected == "Lung Cancer Prediction":

        with col_inputs:
            st.subheader("Input Parameters")
            inputs = [
                display_input(f"Feature {i+1}", "Patient indicator", f"l{i}")
                for i in range(15)
            ]
            predict = st.button("Lung Cancer Test Result")

        with col_result:
            st.subheader("Prediction Result")
            if predict:
                result = models["lungs"].predict([inputs])
                st.success(
                    "Lung Cancer Detected" if result[0] == 1 else "No Lung Cancer"
                )

    # ---------------- THYROID ----------------
    elif selected == "Hypo-Thyroid Prediction":

        with col_inputs:
            st.subheader("Input Parameters")

            age = display_input("Age", "Age", "t1")
            sex = display_input("Sex (1=Male, 0=Female)", "Gender", "t2")
            on_thyroxine = display_input("On Thyroxine", "1=yes,0=no", "t3")
            tsh = display_input("TSH Level", "Hormone level", "t4")
            t3_measured = display_input("T3 Measured", "1=yes,0=no", "t5")
            t3 = display_input("T3 Level", "T3 hormone", "t6")
            tt4 = display_input("TT4 Level", "Total thyroxine", "t7")

            predict = st.button("Thyroid Test Result")

        with col_result:
            st.subheader("Prediction Result")
            if predict:
                result = models["thyroid"].predict([[age, sex, on_thyroxine,
                                                     tsh, t3_measured, t3, tt4]])
                st.success(
                    "Hypo-Thyroid Detected" if result[0] == 1 else "Normal Thyroid"
                )

    # --------------------------------------------------
    # DISCLAIMER
    # --------------------------------------------------
    st.markdown(
        """
        <div class="section-card" style="border-left: 5px solid #ff4b4b;">
        <strong>⚠️ Important Disclaimer</strong><br><br>
        This system is intended strictly for <b>educational and demonstration purposes</b>.
        It must not be used for clinical diagnosis or medical decision-making.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==================================================
# TAB 2 — ABOUT SYSTEM (Placeholder for Phase 3B)
# ==================================================
with tab_about:

    st.header("📊 About the System")

    st.markdown("""
    ### 🧠 1. What is this system?

    The **AI Diagnosis Prediction System** is a machine learning–based decision support application
    designed to demonstrate how predictive models can estimate the *risk likelihood* of certain
    medical conditions based on structured health parameters.

    This system does **not** perform real medical diagnosis.
    Instead, it showcases how trained models respond to clinical-style inputs in a controlled,
    educational environment.
    """)

    st.markdown("""
    ### 🎯 2. Why this system was built

    The primary objective of this project is to:

    - Demonstrate **end-to-end AI system design**
    - Bridge the gap between **machine learning models and user-facing applications**
    - Provide a hands-on example of **ML model deployment**
    - Serve as a **portfolio-grade academic and learning project**

    Many ML projects stop at notebooks.
    This system focuses on **taking trained models into a usable application layer**.
    """)

    st.markdown("""
    ### 🔄 3. How the system works (End-to-End Flow)

    The system follows a structured pipeline:

    1. A user selects a disease category  
    2. The user enters structured clinical parameters  
    3. Input values are passed directly to a pre-trained ML model  
    4. The model performs inference using learned patterns  
    5. A classification result is returned and displayed  

    Each disease prediction is handled by a **separate, independently trained model**,
    ensuring clear separation of logic and responsibility.
    """)

    st.markdown("""
    ### 🤖 4. Machine Learning models used

    The system integrates multiple supervised learning models, including:

    - **Logistic Regression**
    - **Support Vector Machines (SVM)**
    - **Tree-based classifiers**

    Each model was trained on domain-specific datasets containing
    structured health attributes relevant to the corresponding disease.

    Models are serialized and loaded at runtime to enable fast,
    real-time prediction without retraining.
    """)

    st.markdown("""
    ### ⚠️ 5. System limitations

    While this system demonstrates functional AI deployment, it has known limitations:

    - Models are trained on **static datasets**
    - No real-time medical data integration
    - No model retraining or feedback loop
    - Predictions are limited to **binary classification**
    - Input data is assumed to be clean and valid

    These limitations are intentional to keep the system
    focused on demonstration and learning objectives.
    """)

    st.markdown("""
    ### 🛑 6. Ethical & medical disclaimer

    ⚠️ **Important Notice**

    This application is intended **strictly for educational and demonstration purposes**.

    - It must not be used for medical diagnosis
    - It must not replace professional healthcare judgment
    - Predictions should not influence medical decisions

    Always consult qualified healthcare professionals for real medical concerns.
    """)
