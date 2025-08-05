from flask import Flask, render_template, request
import pandas as pd
import joblib
import plotly
import plotly.express as px
import json

app = Flask(__name__)
model = joblib.load("model/weather_model.pkl")
scaler = joblib.load("model/scaler.pkl")

@app.route('/')
def index():
    df = pd.read_csv('weather.csv')
    # Temperature Trend Chart
    fig1 = px.line(df, y=['MaxTemp','MinTemp','Temp3pm'], title="Temperature Trends")
    graph1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # Humidity vs Rainfall
    fig2 = px.scatter(df, x='Humidity3pm', y='Rainfall', opacity=0.6, color_discrete_sequence=['purple'])
    fig2.update_layout(title="Humidity vs Rainfall")
    graph2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graph1=graph1, graph2=graph2)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = ['Humidity3pm','MaxTemp','MinTemp','Temp3pm','WindSpeed9am','WindSpeed3pm','Pressure9am','Pressure3pm']
        values = [float(request.form[feat]) for feat in features]
        scaled = scaler.transform([values])
        prediction = model.predict(scaled)[0]
        return render_template('result.html', prediction=round(prediction, 2))
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
