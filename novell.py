# 채권동적자산배분
# * 3개 : SHY, IEF, TLT, TIP, LQD, HYG, BWX, EMB

import yfinance as yf
import enums
import pandas as pd
import streamlit as st
from dateutil.relativedelta import relativedelta

def build():
    fday = st.session['base_date']
    fday_6mon = fday - relativedelta(months=6)
    data = []
    for v in enums.NovellAsset:
        ticker = v.name
        history = yf.Ticker(ticker).history(start=fday_6mon, end=fday)
        history.index = history.index.date
        history = history[(history.index >= fday_6mon.date()) & (history.index < fday.date())]
        earn = history.Close[-1] / history.Close[0] - 1
        data.append([ticker, earn])

    df = pd.DataFrame(data, columns=['Ticker', 'Score'])
    df.sort_values('Score', ascending=False, inplace=True)
    df.set_index('Ticker', drop=True, inplace=True)
    df['Sign'] = df.Score.apply(lambda x: '😭' if x < 0 else ('🤗' if x >= df.Score[2] else '😶‍🌫️'))
    st.dataframe(df)