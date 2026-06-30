# Solar Flare Prediction Web App

A Machine Learning web application that predicts the risk of severe solar flares using sunspot and solar activity parameters. The project includes data preprocessing, model training with XGBoost, a Flask web interface, REST API, and cloud deployment using Render.

---

## Live Demo

🔗 https://ds-genai-journey.onrender.com

---

## Features

- Predicts severe solar flare risk
- User-friendly Flask web interface
- REST API for predictions
- Machine Learning model using XGBoost
- Responsive futuristic UI
- Cloud deployed on Render

---

## Project Preview

### Home Page
![Home](screenshots/home.png)

### Prediction Result
![Prediction](screenshots/result.png)

---

## Dataset

The dataset contains historical solar active region observations.

Features include:

- Activity
- Evolution
- Previous 24 Hour Flare Activity
- Historically Complex
- Became Complex on this Pass
- Area
- Area of Largest Spot
- Common Flares
- Moderate Flares
- Modified Zurich Class
- Largest Spot Size
- Spot Distribution

Target:

- Severe Flares
    - 0 → Low Risk
    - 1 → High Risk

---

## Machine Learning Pipeline

1. Data Cleaning
2. Remove Duplicates
3. Remove Rare Class
4. One-Hot Encoding
5. Train-Test Split
6. XGBoost Model Training
7. Model Evaluation
8. Save Model using Joblib
9. Flask Integration
10. Deployment on Render

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Flask
- HTML
- CSS
- Jinja2
- Joblib
- Git & GitHub
- Render

---

## Model Performance

Algorithm:

- XGBoost Classifier

Accuracy:

95%

> **Note:** The dataset is highly imbalanced, with very few positive (severe flare) examples. As a result, overall accuracy is high, but predictions for the minority class are limited. This project is intended as a learning and demonstration project.

---

## Project Structure

```
solar-flare-predictor/
│
├── dataset/
│   └── data.csv
│
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── result.html
│
├── app.py
├── train_model.py
├── solar_flare_model.pkl
├── feature_names.pkl
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/sans0726/ds-genai-journey.git
```

Move to project directory

```bash
cd "solar flare predictor"
```

Create virtual environment

```bash
python -m venv ml_env
```

Activate environment

Windows

```bash
ml_env\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask app

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 🌐 API Endpoint

### GET

```
/api
```

Returns

```json
{
  "message": "Welcome to Solar Flare Prediction API",
  "status": "Running",
  "version": "1.0"
}
```

---

### POST

```
/predict_api
```

Example JSON

```json
{
  "activity": 8,
  "evolution": 2,
  "area": 350
}
```

Returns

```json
{
  "prediction": 0,
  "risk": "LOW RISK"
}
```

---

## 📈 Future Improvements

- Better dataset with balanced classes
- Hyperparameter tuning
- Cross Validation
- Probability visualization
- Interactive dashboard
- Real-time NASA Space Weather API integration
- Docker deployment

---

## Author

**Sanskruti**

GitHub:
https://github.com/sans0726

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!