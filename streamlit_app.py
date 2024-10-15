import streamlit as st
import matplotlib.pyplot as plt
import datetime
import plotly.graph_objs as go

import appdirs as ad
ad.user_cache_dir = lambda *args: "/tmp"
import yfinance as yf

# Specify title and logo for the webpage.
# Set up your web app
st.set_page_config(layout="wide", page_title="WebApp_Demo")

# Sidebar
st.sidebar.title("Input")
symbol = st.sidebar.text_input('Please enter the stock symbol: ', 'NVDA').upper()
# Selection for a specific time frame.
col1, col2 = st.sidebar.columns(2, gap="medium")
with col1:
    sdate = st.date_input('Start Date',value=datetime.date(2024,1,1))
with col2:
    edate = st.date_input('End Date',value=datetime.date.today())

st.title(f"{symbol}")

stock = yf.Ticker(symbol)
if stock is not None:
  # Display company's basics
  st.write(f"# Sector : {stock.info['sector']}")
  st.write(f"# Company Beta : {stock.info['beta']}")
else:
  st.error("Failed to fetch historical data.")

data = yf.download(symbol,start=sdate,end=edate)
if data is not None:
  # Create candlestick chart using Plotly
  st.subheader("Candlestick Chart")
  st.markdown("\n\n")
  candlestick = go.Candlestick(x=data.index,open=data['Open'],high=data['High'],low=data['Low'],close=data['Close'])
  layout = go.Layout(xaxis=dict(title='Date'),yaxis=dict(title='Price'),xaxis_rangeslider_visible=False)
  fig = go.Figure(data=[candlestick], layout=layout)
  # Display the chart using Streamlit
  st.plotly_chart(fig,theme='streamlit')
else:
    st.error("Failed to fetch historical data.")
