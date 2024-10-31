import yfinance as yf
import streamlit as st
import mplfinance as mpf
import matplotlib.pyplot as plt

data=yf.download('NVDA')
st.write(data.describe())
