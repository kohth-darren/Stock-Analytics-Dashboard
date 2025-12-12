import matplotlib.pyplot as plt

def plot_price_history(price_df):
    plt.figure(figsize=(12,6))
    for col in price_df.columns:
        plt.plot(price_df.index, price_df[col], label=col)
    plt.title("Price History")
    plt.xlabel("Date")
    plt.ylabel("Adjusted Close Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_cumulative_returns(cum_returns):
    plt.figure(figsize=(12,6))
    for col in cum_returns.columns:
        plt.plot(cum_returns.index, cum_returns[col], label=col)
    plt.title("Cumulative Returns (Growth of $1)")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
