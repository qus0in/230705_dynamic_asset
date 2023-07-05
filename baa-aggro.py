import enums
import common
import streamlit as st

def momentum_score(asset, safe=False):
    base_date = st.session_state['base_date']
    base_date_mo6 = common.month_before(6)
    base_date_mo12 = common.month_before(12)

    # print(asset.name)
    ticker = yf.Ticker(asset.name)
    history = common.get_history(common.month_before(12), base_date)
    # print(history.Close)
    if safe: return history.Close.iloc[-1] / history.Close.mean()
    history.index = history.index.date
    filter_mo = lambda x: history[history.index >= mo(x)].Close
    score_mo = lambda x: filter_mo(x).iloc[-1] / filter_mo(x).iloc[0] - 1
    span = [1, 3, 6, 12]
    score = sum([score_mo(s) * 12 / s for s in span])
    return score

def check_canary():
    for asset in CanaryAsset:
        if momentum_score(asset) <= 0:
            return False
    return True

def cal_aggro():
    aggro = pd.DataFrame(
        [(asset.name, momentum_score(asset))
        for asset in AggroAsset],
        columns=['Ticker', 'Score']
    ).sort_values('Score', ascending=False
    ).set_index('Ticker')
    aggro['Sign'] = aggro.Score.apply(
        lambda x: '😭' if x <= 0 else ('👑' if x >= aggro.Score[0] else '😶‍🌫️'))
    return aggro

def cal_safe():
    safe = pd.DataFrame(
        [(asset.name, momentum_score(asset, True))
        for asset in SafeAsset],
        columns=['Ticker', 'Score']
    ).sort_values('Score', ascending=False
    ).set_index('Ticker')
    safe['Sign'] = safe.Score.apply(
        lambda x: '☔' if x <= 1 else ('☀️' if x >= safe.Score[2] else '☁️'))
    return safe

def build():
    df = None
    if check_canary():
        df = cal_aggro()
    else:
        df = cal_safe()

    st.write("""
    ## BAA 공격형
    * 1개 : QQQ, VEA, VWO, BND
    * 3개 : TIP, PDBC, IEF, TLT, LQD, BND
    """)
    st.dataframe(df)
    
main()