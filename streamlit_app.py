import streamlit as st
import matplotlib.pyplot as plt
import datetime
import yfinance as yf
import pandas as pd
import pandas_ta as ta
import mplfinance as mpf
import plotly.graph_objs as go
import appdirs as ad
ad.user_cache_dir = lambda *args: "/tmp"

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
data.columns = pd.Index(['Adj Close','Close','High','Low','Open','Volume'])
if data is not None:
    colors = mpf.marketcolors(up='lime',down='r',wick={'up':'lime','down':'r'},edge={'up':'lime','down':'r'},volume={'up':'lime','down':'r'})
    s = mpf.make_mpf_style(marketcolors=colors,facecolor='black',edgecolor='w')
    fig,ax=mpf.plot(data,style='s')
    st.pyplot(fig)
else:
    st.error("Failed to fetch historical data.")
