import datetime as dt
import streamlit as st

from fetch_data import fetch_price_data
from compute_metrics import (
    compute_daily_returns,
    compute_cumulative_returns,
    compute_statistics,
)

st.set_page_config(
    page_title="Stock Analytics Dashboard", #title on browser tab
    layout="wide" #maximize width of the page
)

st.title("📈 Stock Analytics Dashboard") #title shown at top of webpage
st.write("""
Analyze stocks using real Yahoo Finance data.

1. Enter your preferred tickers  
2. Choose a start date  
3. View returns, volatility, and Sharpe ratios  

Developed by Darren K.
""")

def clean_ticker_input(raw: str):
    tickers = raw.split(",")                    # split user input by commas
    tickers = [t.strip() for t in tickers]      # remove extra spaces
    tickers = [t.upper() for t in tickers]      # convert symbols to uppercase
    tickers = [t for t in tickers if t != ""]   # remove empty entries
    return tickers

st.sidebar.header("⚙️ Settings")

tickers_input = st.sidebar.text_input(
    "Enter Tickers (comma separated):",
    placeholder="e.g. AAPL, MSFT, NVDA",
)

start_date = st.sidebar.date_input(
    "Select start date",
    value=dt.date(2015, 1, 1)   # default start date
)

risk_free_pct = st.sidebar.slider(
    "Annual risk-free rate (%)",
    min_value=0.00,
    max_value=10.00,
    value=2.00,
    step=0.01,
    format="%.2f",
)

run_button = st.sidebar.button("Run Analysis 🚀")

if run_button:

    tickers = clean_ticker_input(tickers_input)

    if not tickers: #if user clicked "Run" without entering any tickers
        st.error("Please enter at least one valid ticker symbol.")

    else:
        try:
            st.subheader("1️⃣ Price Data")

            with st.spinner("Fetching data from Yahoo Finance..."):
                prices = fetch_price_data(tickers, start=str(start_date))

            if prices.empty:
                st.error("No price data returned. Check tickers or date range.")

            else:
                st.write(
                    f"Data from **{prices.index.min().date()}** "
                    f"to **{prices.index.max().date()}**"
                )

                display_prices = prices.copy()
                display_prices.index = display_prices.index.strftime("%Y-%m-%d")

                st.dataframe(display_prices.tail())

                st.subheader("2️⃣ Performance Metrics: Annual Returns, Volatility, Sharpe Ratios")
                daily_returns = compute_daily_returns(prices)
                cum_returns = compute_cumulative_returns(daily_returns)
                
                stats = compute_statistics(
                    daily_returns,
                    risk_free_rate=risk_free_pct / 100
                )

                st.dataframe(
                    stats.style.format({
                        "Annual Return": "{:.2%}",
                        "Annual Volatility": "{:.2%}",
                        "Sharpe Ratio": "{:.2f}"
                    })
                )

                st.subheader("3️⃣ Charts")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("**Price History**")
                    st.line_chart(prices)

                with col2:
                    st.markdown("**Cumulative Returns (Growth of $1)**")
                    st.line_chart(cum_returns)

        except Exception as e:
            st.error(f"Something went wrong: {e}") #unexpected error to prevent app crash
            st.stop()

else:
    st.info("👈 Enter tickers and click **Run Analysis** to start.")
