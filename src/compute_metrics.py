import numpy as np
import pandas as pd

def compute_daily_returns(price_df):
    daily_returns = price_df.pct_change() #computes daily %R for each stock
    daily_returns = daily_returns.dropna() #removing NaN values
    return daily_returns

def compute_cumulative_returns(daily_returns):
    growth_factor = 1 + daily_returns #adds 1 to each daily return value
    cumulative_returns = growth_factor.cumprod() #cumulative product over time (total growth)
    return cumulative_returns


def compute_statistics(daily_returns, risk_free_rate=0.02):
    avg_daily_return = daily_returns.mean() #computes avg daily return for each stock
    daily_volatility = daily_returns.std() #computes std dev of daily returns for each stock (daily volatility)
    
    annual_return = (1 + avg_daily_return) ** 252 - 1 #annualized return (assuming 252 trading days)
    annual_volatility = daily_volatility * np.sqrt(252)
    
    sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility #computes sharpe ratio [Sharpe Ratio = (Return - Risk-free) / Volatility)]
    
    stats_df = pd.DataFrame({
        "Annual Return": annual_return,
        "Annual Volatility": annual_volatility,
        "Sharpe Ratio": sharpe_ratio
    })
    
    stats_df = stats_df.sort_values("Sharpe Ratio", ascending=False) #sorting stocks from best-wosrt based on sharpe ratio
    
    return stats_df
