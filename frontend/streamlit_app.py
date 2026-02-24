import streamlit as st
import requests

st.set_page_config(page_title="Emotion Classifier", layout="centered")

st.title("🧠 Emotion Classification App")

user_input = st.text_area("Enter your text:")

if st.button("Predict Emotion"):

    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
        response = requests.post(
            "http://<EC2_PUBLIC_IP>:8000",
            json={"text": user_input}
        )

        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Emotion: {result['predicted_emotion']}")
            st.info(f"Confidence: {result['confidence']}")
        else:
            st.error("Error connecting to backend")