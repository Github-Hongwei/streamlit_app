from datetime import date, timedelta, datetime
import streamlit as st
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

data=yf.download('NVDA')
data.index = pd.to_datetime(data['timestamp'], unit = 'ms')

fig = mpf.figure(style='yahoo', figsize=(8,6))
mpf.plot(data)
st.pyplot(fig)
