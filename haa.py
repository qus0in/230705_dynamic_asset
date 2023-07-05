import enums
import common
import streamlit as st

def check_canary():
    for asset in enums.HAACanaryAsset:
        if common.momentum_score(asset, weight=False) <= 0:
            return False
    return True

def cal_aggro():
    data = [(asset.name, common.momentum_score(asset, weight=False)) for asset in enums.HAAAggroAsset] 
    handler = lambda y : lambda x: '😭' if x <= 0 else ('👑' if x >= y.Score[3] else '😶‍🌫️')
    return common.dataframe(data, handler)

def cal_safe():
    data = [(asset.name, common.momentum_score(asset, safe=True, weight=False)) for asset in enums.HAASafeAsset] 
    handler = lambda y : lambda x: '☔' if x <= 1 else ('☀️' if x >= y.Score[0] else '☁️')
    return common.dataframe(data, handler)

def build():
    st.write("""
    ## HAA
    * 4개 : SPY, IWM, VEA, VWO, VNQ, PDBC, IEF, TLT
    """)
    if check_canary():
        cal_aggro()
    else:
        cal_safe()