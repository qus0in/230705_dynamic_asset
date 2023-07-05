# 채권동적자산배분
# * 3개 : SHY, IEF, TLT, TIP, LQD, HYG, BWX, EMB

import enums
import common
import pandas as pd
import streamlit as st

def build():
    base_date = st.session['base_date']
    base_date_mo6 = common.month_before(6)
    base_date_mo12 = common.month_before(12)

    data = []
    for v in enums.NovellAsset:
        ticker = v.name
        history = common.get_history(ticker, base_date_mo12, base_date)
        history = history[(history.index >= base_date_mo6.date()) & (history.index < base_date.date())]
        earn = history.Close[-1] / history.Close[0] - 1
        data.append([ticker, earn])

    df = pd.DataFrame(data, columns=['Ticker', 'Score'])
    df.sort_values('Score', ascending=False, inplace=True)
    df.set_index('Ticker', drop=True, inplace=True)
    df['Sign'] = df.Score.apply(lambda x: '😭' if x < 0 else ('🤗' if x >= df.Score[2] else '😶‍🌫️'))
    st.dataframe(df)