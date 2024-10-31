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

symbol = st.text_input('Please enter the stock symbol: ', 'NVDA').upper()

st.title(f"{symbol}")
df=yf.download(symbol,start="2024-01-01",end="2024-09-30")
st.write(df['Close'])
#fig = go.Figure(data=[go.Candlestick(x=df.index,
#                                     open=df['Open'],
#                                     high=df['High'],
#                                     low=df['Low'],
#                                     close=df['Close'])])

#fig.update_layout(xaxis_rangeslider_visible=False)
#st.plotly_chart(fig, theme='streamlit')
