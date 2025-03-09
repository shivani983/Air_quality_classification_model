# 🌍 Air Quality Classification Model

## 📌 Overview
This project is an **Air Quality Classification Model** built using Machine Learning. It features a Streamlit-based UI where users can select an ML model and input data for air quality prediction. The app loads multiple trained models from `.pkl` files using joblib.

## ✨ Features
- ✅ Multiple ML models available (SVC, Logistic Regression, etc.)
- ✅ User-friendly UI using Streamlit
- ✅ Model selection for prediction
- ✅ Pre-trained models loaded via joblib
- ✅ Supports binary and multi-class classification

## 📂 Project Structure
```plaintext
Air Quality Classification Model/
│-- models/
│   │-- svc_binary.pkl
│   │-- svc_multi.pkl
│   │-- logistic_binary.pkl
│   │-- logistic_ovr.pkl
│   │-- logistic_multi.pkl
│   │-- encoder.pkl
│-- setup.py
│-- app.py
│-- requirements.txt
│-- README.md
```

## 🚀 Installation & Setup
### 1️⃣ Create a Virtual Environment
```bash
python -m venv env
```
#### Activate Virtual Environment:
- **Windows**: `env\Scripts\activate`
- **Mac/Linux**: `source env/bin/activate`

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

## 🔧 Usage
1. Open the Streamlit UI in your browser.
2. Select an ML model from the dropdown.
3. Enter data for air quality classification.
4. Click **"Predict"** to get results.

## 📦 Dependencies
- **streamlit**
- **pandas**
- **scikit-learn**
- **joblib**
- **numpy**

## 💾 Saving and Loading Models
### Saving models:
```python
import joblib
joblib.dump(model, 'model.pkl')
```
### Loading models:
```python
model = joblib.load('model.pkl')
prediction = model.predict(data)
```

## ❗ Troubleshooting
- **Issue:** `NameError: name 'svc_binary' is not defined`
  - ✅ **Fix:** Ensure models are loaded using `joblib.load('svc_binary.pkl')` before calling them.
- **Issue:** `FileNotFoundError: Model file not found`
  - ✅ **Fix:** Check if `.pkl` files exist in the `models/` directory.

## 🤝 Contributing
Feel free to fork this repository and submit pull requests (PRs) with improvements! 🚀

## 📜 License
This project is licensed under the **MIT License**.

---
### 💡 Developed by **Shivani Virang** 🚀
