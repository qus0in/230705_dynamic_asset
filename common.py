from dateutil.relativedelta import relativedelta
import yfinance as yf

def month_before(date, months):
    return date - relativedelta(months=months)

@st.cache_data
def get_history(ticker, start_date, end_date):
    history = yf.Ticker(ticker).history(start=base_date_mo12, end=base_date)
    history.index = history.index.date
    return history