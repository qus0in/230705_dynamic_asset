import enums
import common
import streamlit as st

def check_canary():
    for asset in enums.BAACanaryAsset:
        if common.momentum_score(asset) <= 0:
            return False
    return True

def cal_aggro():
    data = [(asset.name, common.momentum_score(asset)) for asset in enums.BAAAggroAsset] 
    handler = lambda y : lambda x: '😭' if x <= 0 else ('👑' if x >= y.Score[0] else '😶‍🌫️')
    return common.dataframe(data, handler)

def cal_safe():
    data = [(asset.name, common.momentum_score(asset, safe=True)) for asset in enums.BAASafeAsset] 
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