# 🌍 Air Quality Classification Model

📌 Overview

This project is an Air Quality Classification Model built using Machine Learning. It provides a Streamlit-based UI where users can select an ML model and input data for air quality prediction. The app loads multiple trained models from .pkl files using joblib.

# ✨ Features

✅ Multiple ML models available (SVC, Logistic Regression, etc.)
✅ User-friendly UI using Streamlit
✅ Model selection for prediction
✅ Pre-trained models loaded via joblib
✅ Supports binary and multi-class classification

# 📂 Project Structure

 Air Quality Classification Model/ 
 
│-- models/
│   │-- svc_binary.pkl
│   │-- svc_multi.pkl
│   │-- logistic_binary.pkl
│   │-- logistic_ovr.pkl
│   │-- logistic_multi.pkl
│   │-- encoder.pkl
│   │-- setup.py
│   │-- app.py
│-- requirements.txt
│-- README.md 

# 🚀 Installation & Setup

 1️⃣ Create a Virtual Environment

 python -m venv env

 Activate Virtual Environment:
 Windows: env\Scripts\activate

Mac/Linux: source env/bin/activate

# 2️⃣ Install Dependencies

 pip install -r requirements.txt

# 3️⃣ Run the Streamlit App

streamlit run app.py

## 🔧 Usage

1️⃣ Open the Streamlit UI in your browser.
 2️⃣ Select an ML model from the dropdown.
 3️⃣ Enter data for air quality classification.
 4️⃣ Click "Predict" to get results.

# 📦 Dependencies

 streamlit

 pandas

 scikit-learn

 joblib

numpy

# 💾 Saving and Loading Models

## Saving models:

 import joblib
 joblib.dump(model, 'model.pkl')

## Loading models:

 model = joblib.load('model.pkl')
 prediction = model.predict(data)

# ❗ Troubleshooting

🔹 Issue: NameError: name 'svc_binary' is not defined

 ✅ Fix: Ensure models are loaded using joblib.load('svc_binary.pkl') before calling them.

 🔹 Issue: FileNotFoundError: Model file not found

 ✅ Fix: Check if .pkl files exist in the models/ directory.

## 🤝 Contributing

 Feel free to fork this repository and submit pull requests (PRs) with improvements! 🚀

## 📜 License
 This project is licensed under the MIT License.

# 💡 Developed by Shivani Virang 🚀
# Air Quality Classification Model

This project provides a Streamlit-based web application for predicting air quality using various machine learning models.

## Folder Structure

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

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/air-quality-classification.git
   cd air-quality-classification
   ```
2. Create a virtual environment and activate it:
   ```bash
   conda create --name air_quality_env python=3.10
   conda activate air_quality_env
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Model Information
- **Support Vector Classifier (SVC)**: Binary and multi-class models
- **Logistic Regression**: Binary, OVR, and multinomial classification models
- **Encoder**: Used for preprocessing categorical features

## Contributing
Feel free to fork this repository and submit pull requests with improvements.

## License
This project is licensed under the MIT License.
