import numpy as np
import pandas as pd
import yfinance as yf
from keras.models import load_model
import matplotlib.pyplot as plt
import streamlit as st

model = load_model(r'D:\StockPricePrediction\Stock_prediction_model.keras')

st.header('Stock Market Predictior')
stock = st.text_input('Enter Tock Symbol','GOOG')

start = '2010-01-01'
end = '2024-12-31'

data = yf.download(stock,start,end)

st.subheader('Stock Data')
st.write(data)

data_train = pd.DataFrame(data.Close[0:int(len(data)*0.80)])
data_test = pd.DataFrame(data.Close[int(len(data)*0.80):len(data)])

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))

pas_100 = data_train.tail(100)
data_test = pd.concat([pas_100,data_test],ignore_index=True)
data_testScale = scaler.fit_transform(data_test)

x=[]
y=[]
for i in range(100,data_testScale.shape[0]):
    x.append(data_testScale[i-100:i])
    y.append(data_testScale[i,0])

x,y=np.array(x),np.array(y)

st.subheader('Price vs MA50')
mav_50 = data.Close.rolling(50).mean()
fig = plt.figure(figsize=(8,6))
plt.plot(mav_50,'r',label='moving average 50')
plt.plot(data.Close,'b',label='Price')
plt.legend()
plt.show()
st.pyplot(fig)

st.subheader('Price vs MA50 vs MA100')
mav_100 = data.Close.rolling(100).mean()
fig1 = plt.figure(figsize=(8,6))
plt.plot(mav_50,'r',label='moving average 50')
plt.plot(mav_100,'g',label='moving average 100')
plt.plot(data.Close,'b',label='Price')
plt.legend()
plt.show()
st.pyplot(fig1)

st.subheader('Price vs MA100 vs MA200')
mav_200 = data.Close.rolling(200).mean()
fig2 = plt.figure(figsize=(8,6))
plt.plot(mav_100,'r',label='moving average 100')
plt.plot(mav_200,'g',label='moving average 200')
plt.plot(data.Close,'b',label='Price')
plt.legend()
plt.show()
st.pyplot(fig2)



#st.write(data)

predict = model.predict(x)

scale = scaler.scale_

predict = predict * scale

y=y*scale

st.subheader('Actual Price Vs Predicted Price')
fig3 = plt.figure(figsize=(8,6))
plt.plot(y,'b',label='Original Price')
plt.plot(predict,'r',label='Predicted Price')
plt.xlabel('time')
plt.ylabel('Price')
plt.legend()
plt.show()
st.pyplot(fig3)