# Stock Analytics Dashboard

This project is a simple stock analysis tool built with Python and Streamlit.  
It retrieves historical stock data using the Yahoo Finance API and computes  
basic performance metrics such as daily returns, annualized return, volatility,  
and the Sharpe ratio. The dashboard also provides interactive charts for  
visualizing price history and cumulative returns.

# Features:
- Fetch historical stock data using yfinance
- Calculate daily returns
- Compute annualized return and annualized volatility
- Compute Sharpe ratio
- Display price and cumulative return charts
- User inputs for tickers, start date, and risk-free rate

# Technologies Utilized:
- Python
- Streamlit
- Pandas
- NumPy
- yfinance
- Matplotlib

# How to Run:
1. Clone the repository:
   git clone https://github.com/kohth-darren/Stock-Analytics-Dashboard.git

2. Install dependencies:
   pip install -r requirements.txt

3. Run the dashboard:
   streamlit run src/dashboard.py

# Author
Developed by Darren K.
