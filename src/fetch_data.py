import yfinance as yf
import pandas as pd


def fetch_price_data(tickers, start):
    data = yf.download(
        tickers,
        start=start,
        auto_adjust=False,
        progress=False
    )

    adj_close = data["Adj Close"]
    adj_close = adj_close.dropna(how="all")

    if isinstance(adj_close, pd.Series):
        adj_close = adj_close.to_frame(name=tickers[0])

    return adj_close