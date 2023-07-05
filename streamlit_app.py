from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st

import novell
import baa_aggro
import haa

def main():
    with st.sidebar:
        label = "기준월"
        month_slider = st.slider(label, min_value=0, max_value=12, value=0, step=1, format="%d개월 전")
        slider_date = datetime.today() - relativedelta(months=month_slider)
        st.subheader(f"{slider_date.year}년 {slider_date.month}월")
        st.session_state['base_date'] = datetime(slider_date.year, slider_date.month, 1) - relativedelta(days=1)
        # st.write(st.session_state['base_date'])

    tabs = st.tabs(["Novell", "BAA 공격형", "HAA"])
    with tabs[0]:
        novell.build()
    with tabs[1]:
        baa_aggro.build()
    with tabs[2]:
        haa.build()

if __name__ == '__main__':
    main()