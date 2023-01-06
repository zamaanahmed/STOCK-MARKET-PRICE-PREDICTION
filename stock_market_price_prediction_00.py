# -*- coding: utf-8 -*-
"""STOCK MARKET PRICE PREDICTION-00

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PIb-r1s35nSrfXPrsy_gENFtMU_oWh_2
"""

!pip install streamlit
!pip install yfinance
!pip install pystan~=2.14
!pip install fbprophet

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# from datetime import date
# import yfinance as yf
# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly
# from plotly import graph_objs as go
# # up and ready for development
# 
# start = "2017-01-01"
# today = date.today().strftime("%Y-%m-%d")
# st.title("STOCK PRICE PREDICTOR")
# stocks = ('TTM', 'RELI', 'IBM', 'SBIN.NS', 'MSFT')
# selected_stocks = st.selectbox("selected dataset for the prediction", stocks)
# n_years = st.slider("Select number of years",1,4)
# period = n_years*365
# 
# 
# #end of part 1 
# 
# 
# def load_data(ticker):
#   data = yf.download(ticker,start,today)
#   data.reset_index(inplace=True)
#   return data
# 
# 
# data_load_state = st.text("loading data")
# data = load_data(selected_stocks)
# data_load_state.text("loading data....done")
# 
# #end of part 2 
# 
# st.subheader("RAW DATA")
# st.write(data.head())
# 
# def plot_raw_data():
#   fig = go.Figure()
#   fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'],name="Open stock"))
#   fig.add_trace(go.Scatter(x=data['Date'],y=data['Close'],name="Close stock"))
#   st.plotly_chart(fig)
#   fig.layout.update(title_text='Time series with rangeslider',xaxis_rangeslider_visible=True)
#   st.plotly_chart(fig)
# 
# 
# plot_raw_data()
# 
# #end of part 3
# 
# df_train = data[['Date','Close']]
# df_train = df_train.rename(columns={"Date": "ds","Close":"y"})
# 
# m = Prophet()
# m.fit(df_train)
# future = m.make_future_dataframe(periods=period)
# 
# forecast = m.predict(future)
# 
# #end of part 4
# 
# st.subheader("Forecast Data")
# st.write(forecast.tail())
# 
# st.write(f"Forecast plot for {n_years} years")
# fig1 = plot_plotly(m,forecast)
# st.plotly_chart(fig1)
# 
# #end of part 5
#

!streamlit run app.py & npx localtunnel --port 8501