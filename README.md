# 🎭 Emotion Detector Pro™

> Let AI vibe-check your texts 🔥

![streamlit badge](https://img.shields.io/badge/Built%20With-Streamlit-red?style=for-the-badge&logo=streamlit)
![python badge](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![vibe badge](https://img.shields.io/badge/Vibe-Checked💯-purple?style=for-the-badge)

---

## 🧠 What Is This?

A cool little app that reads your message and tells you what kind of emotion it carries — powered by AI, trained on real data, and wrapped in a 🔥 Streamlit interface.

Wanna know if your ex’s message is fake love or real anger? Paste it. We gotchu. 💔➡️🔥

---

## 🚀 How It Works

1. Your message gets cleaned like it’s heading to a date 🧼
2. It gets vectorized with TF-IDF (because words matter)
3. A Logistic Regression model makes the prediction
4. BOOM — Emotion served on a silver plate

---

## 🧪 Tech Stack

- 🐍 **Python**
- 📦 **scikit-learn** for model
- 📊 **TF-IDF Vectorizer** for feature extraction
- 🧹 **NLTK** for stopwords & tokenizing
- 🖥️ **Streamlit** for the fancy UI
- 💾 **Joblib** for model loading

---

## 🎯 Emotions It Can Detect:

| Label No. | Emotion   |
|-----------|-----------|
| 0         | Happy 😊  |
| 1         | Sad 😢    |
| 2         | Anger 😠  |
| 3         | Love ❤️  |
| 4         | Fear 😨   |
| 5         | Surprise 😲 |

---

## 🛠️ How To Run Locally

```bash
git clone https://github.com/your-username/emotion-detector-pro.git
cd emotion-detector-pro
pip install -r requirements.txt
streamlit run app.py
