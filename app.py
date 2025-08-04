import streamlit as st
import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import joblib

import os
base_dir = os.path.dirname(os.path.abspath(__file__))
vectorizer = joblib.load(os.path.join(base_dir, "tfidf_vectorizer.pkl"))
model = joblib.load(os.path.join(base_dir, "logistic_model.pkl"))
label_map = joblib.load(os.path.join(base_dir, "label_map.pkl"))
inv_label_map = {v: k for k, v in label_map.items()}



nltk.download('punkt')
nltk.download('stopwords')


def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ''.join([c for c in text if not c.isdigit()])
    text = ''.join([c for c in text if c.isascii()])
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered = [word for word in words if word not in stop_words]
    return ' '.join(filtered)




st.set_page_config(page_title="Emotion Detector Pro™", page_icon="🎭")

st.markdown("""
    <div style="text-align: center;">
        <h1 style="color:#6C63FF;">🎭 Emotion Detector Pro™</h1>
        <p style="color:#555;">Let AI detect the vibe of your text</p>
    </div>
""", unsafe_allow_html=True)

user_input = st.text_area("🔍 Enter your message:", placeholder="e.g., I'm so happy today!")

if st.button("Predict Emotion"):
    if user_input.strip() == "":
        st.warning("Text field is empty. Type something to test.")
    else:
        cleaned_text = preprocess(user_input)
        vec_input = vectorizer.transform([cleaned_text])
        prediction = model.predict(vec_input)[0]
        predicted_emotion = inv_label_map[prediction]

        
        st.success(f"🎉 Detected Emotion: **{predicted_emotion.upper()}**")

        st.markdown("""
        <style>
        .st-success {
            background-color: #E0F7FA;
            border-left: 5px solid #00BCD4;
            padding: 10px;
            font-size: 18px;
        }
        </style>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<center style='font-size:13px; color:gray;'>Made with 💙 by Shaheer</center>", unsafe_allow_html=True)
