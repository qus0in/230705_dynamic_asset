from dateutil.relativedelta import relativedelta
import yfinance as yf
import streamlit as st

def month_before(months):
    return st.session_state.base_date - relativedelta(months=months)

@st.cache_data
def get_history(ticker, start_date, end_date):
    history = yf.Ticker(ticker).history(start=start_date, end=end_date)
    history.index = history.index.date
    return history

def dataframe(data, sign_handler):
    df = pd.DataFrame(data, columns=['Ticker', 'Score'])
    df.sort_values('Score', ascending=False, inplace=True)
    df.set_index('Ticker', drop=True, inplace=True)
    df['Sign'] = df.Score.apply(sign_handler)
    st.dataframe(df)