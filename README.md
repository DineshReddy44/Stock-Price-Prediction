# 📈 Stock Price Prediction

A machine learning-based web application that predicts stock prices using historical market data and deep learning techniques.

---

## 📌 Overview

This project uses historical stock price data to analyze trends and predict future prices. It leverages a trained deep learning model to forecast stock movements and visualize insights through an interactive web application.

---

## 🚀 Features

- 📊 Real-time stock data fetching using Yahoo Finance  
- 📉 Visualization of stock trends  
- 📈 Moving averages (MA50, MA100, MA200) analysis  
- 🤖 Deep learning model for price prediction  
- 📌 Comparison of actual vs predicted prices  
- ⚡ Interactive UI built with Streamlit  

---

## 🧠 How It Works

The application performs the following steps:

- Fetches historical stock data using yfinance :contentReference[oaicite:0]{index=0}  
- Splits data into training and testing sets  
- Scales data using MinMaxScaler  
- Uses past 100 days of data to predict future prices  
- Loads a pre-trained Keras model (`Stock_prediction_model.keras`)  
- Generates predictions and compares them with actual values  

---

## ⚙️ Tech Stack

- Python  
- NumPy  
- Pandas  
- Matplotlib  
- Scikit-learn  
- TensorFlow / Keras  
- Streamlit  
- yfinance  

---

## 📂 Project Structure
Stock-Price-Prediction/
│
├── app.py
├── Stock_prediction_model.keras
├── StockPrediction.ipynb
└── README.md



---

## ▶️ How to Run

1. Clone the repository
    git clone https://github.com/your-username/Stock-Price-Prediction.git
    cd Stock-Price-Prediction


2. Install dependencies
    pip install -r requirements.txt


3. Run the application
    streamlit run app.py


---

## 📊 Visualizations

- Stock closing price trends  
- Moving averages (50, 100, 200 days)  
- Actual vs Predicted stock prices  

---

## 🎯 Future Improvements

- Add support for multiple stocks comparison  
- Improve model accuracy with advanced architectures (LSTM/GRU tuning)  
- Deploy the application online  
- Integrate real-time prediction updates  

---

## 👨‍💻 Author

Dinesh Reddy