from dateutil.relativedelta import relativedelta
import yfinance as yf
import streamlit as st

def month_before(base_date, months):
    return base_date - relativedelta(months=months)

@st.cache_data
def get_history(ticker, start_date, end_date):
    history = yf.Ticker(ticker).history(start=start_date, end=end_date)
    history.index = history.index.date
    return history