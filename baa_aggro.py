import enums
import common
import streamlit as st

def momentum_score(asset, safe=False):
    base_date = st.session_state['base_date']
    
    history = common.get_history(asset.name, common.month_before(12), base_date)
    if safe:
        return history.Close.iloc[-1] / history.Close.mean()

    filter_mo = lambda x: history[history.index >= common.month_before(x).date()].Close
    score_mo = lambda x: filter_mo(x).iloc[-1] / filter_mo(x).iloc[0] - 1
    span = [1, 3, 6, 12]
    score = sum([score_mo(s) * 12 / s for s in span])
    return score

def check_canary():
    for asset in enums.BAACanaryAsset:
        if momentum_score(asset) <= 0:
            return False
    return True

def cal_aggro():
    data = [(asset.name, momentum_score(asset)) for asset in enums.BAAAggroAsset] 
    handler = lambda y : lambda x: '😭' if x <= 0 else ('👑' if x >= y.Score[0] else '😶‍🌫️')
    return common.dataframe(data, handler)

def cal_safe():
    data = [(asset.name, momentum_score(asset)) for asset in enums.BAASafeAsset] 
    handler = lambda y : lambda x: '☔' if x <= 1 else ('☀️' if x >= y.Score[2] else '☁️')
    return common.dataframe(data, handler)

def build():
    st.write("""
    ## BAA 공격형
    * 1개 : QQQ, VEA, VWO, BND
    * 3개 : TIP, PDBC, IEF, TLT, LQD, BND
    """)
    if check_canary():
        cal_aggro()
    else:
        cal_safe()