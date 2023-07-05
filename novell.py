# 채권동적자산배분
# * 3개 : SHY, IEF, TLT, TIP, LQD, HYG, BWX, EMB

import yfinance as yf
from enum import Enum, auto
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import streamlit as st

class Asset(Enum):
    SHY = auto()
    IEF = auto()
    TLT = auto()
    TIP = auto()
    LQD = auto()
    HYG = auto()
    BWX = auto()
    EMB = auto()

def build():
    pd.options.display.float_format = '{:.3f}'.format
    slider = 0
    today = datetime.today() - relativedelta(months=slider)
    fday = datetime(today.year, today.month, 1)
    fday_6mon = fday - relativedelta(months=6)
    print(f"{fday.year}년 {fday.month}월")

    data = []
    for v in Asset:
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