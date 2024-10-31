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
# if stock is not None:
#   # Display company's basics
#   st.write(f"# Sector : {stock.info['sector']}")
# else:
#   st.error("Failed to fetch historical data.")

spy_History = stock.history(period='5d')

fig = go.Figure(data=[go.Candlestick(x=spy_History.index,
                                     open=spy_History['Open'],
                                     high=spy_History['High'],
                                     low=spy_History['Low'],
                                     close=spy_History['Close'])])

fig.update_layout(xaxis_rangeslider_visible=False)
st.plotly_chart(fig, theme='streamlit')
