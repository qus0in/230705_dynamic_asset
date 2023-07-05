from dateutil.relativedelta import relativedelta
import pandas as pd
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
    df['Sign'] = df.Score.apply(sign_handler(df))
    st.dataframe(df)

def momentum_score(asset, safe=False, weight=True):
    base_date = st.session_state['base_date']

    history = get_history(asset.name, month_before(12), base_date)
    if safe:
        return history.Close.iloc[-1] / history.Close.mean()

    filter_mo = lambda x: history[history.index > month_before(x).date()].Close
    score_mo = lambda x: filter_mo(x).iloc[-1] / filter_mo(x).iloc[0] - 1
    span = [1, 3, 6, 12]
    return sum([score_mo(s) * 12 / s for s in span]) if weight else sum([score_mo(s) * 12 for s in span])