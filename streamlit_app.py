import yfinance as yf
import streamlit as st
import mplfinance as mpf
import matplotlib.pyplot as plt

data=yf.download('NVDA')
fig = mpf.figure(style='yahoo', figsize=(8,6))
mpf.plot(data)
st.pyplot(fig)
