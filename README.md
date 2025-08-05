### Weather Data Analysis & Rainfall Prediction Web App
## Overview
This is a Flask-based web application for visualizing weather trends and predicting rainfall using machine learning.
It provides:
Interactive temperature & humidity charts
Rainfall prediction using a trained Random Forest model
Simple form-based input for prediction

## Features
Interactive Charts using Plotly:
Temperature trends (Max, Min, 3PM Temp)
Humidity vs Rainfall correlation

Machine Learning Model:
Random Forest regression trained on weather data
StandardScaler preprocessing for consistent inputs

Web Interface:
Bootstrap-based responsive UI

Simple form to input weather conditions and get rainfall predictions

## Installation & Usage
Clone repository & enter folder
git clone https://github.com/sabnam813/Weather-Analysis-Prediction-.git
cd weather_app

Create & activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

Install dependencies
pip install -r requirements.txt

Train model
python train_model.py

Run Flask app
python app.py

Open browser
http://127.0.0.1:5000

## License
This project is licensed under the MIT License - see the LICENSE file for details.
