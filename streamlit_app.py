from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import novell

def main():
    with st.slider:
        label = "기준월"
        month_slider = st.slider(label, min_value=0, max_value=12, value=0, step=1, format="%d개월 전".format)
        base_date = datetime.today() - relativedelta(months=month_slider)
        st.subheader(f"{base_date.year}년 {base_date.month}월")
        st.session['base_date'] = datetime(today.year, today.month, 1)

    tabs = ["Novell"]
    with tabs[0]:
        novell.build()

if __name__ == '__main__':
    main()