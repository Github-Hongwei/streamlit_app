from datetime import date, timedelta, datetime
import streamlit as st
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

def get_historical_data(symbol, start_date = None):
    df = pdr.get_data_yahoo(symbol, start=start_date, end=datetime.now())
    df = df.rename(columns = {'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Adj Close': 'adj close', 'Volume': 'volume'})
    for i in df.columns:
        df[i] = df[i].astype(float)
    df.index = pd.to_datetime(df.index)
    if start_date:
        df = df[df.index >= start_date]
    return df

hist = get_historical_data('AAPL', '2021-01-01')

fig = mpf.figure(style='yahoo', figsize=(8,6))
mpf.plot(hist)
st.pyplot(fig)
