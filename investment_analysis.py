
```python
import pandas as pd

def calculate_returns(prices):
    returns = prices.pct_change()
    return returns

def calculate_volatility(returns):
    volatility = returns.std() * (252 ** 0.5)
    return volatility

def calculate_sharpe_ratio(returns, risk_free_rate):
    average_returns = returns.mean() * 252
    standard_deviation = returns.std() * (252 ** 0.5)
    sharpe_ratio = (average_returns - risk_free_rate) / standard_deviation
    return sharpe_ratio

def main():
    # Read investment data
    data = pd.read_csv('investment_data.csv')

    # Calculate returns
    prices = data['Price']
    returns = calculate_returns(prices)
    
    # Calculate volatility
    volatility = calculate_volatility(returns)
    print(f"Volatility: {volatility}")
    
    # Calculate Sharpe Ratio
    risk_free_rate = 0.05 # Assume 5% risk-free rate
    sharpe_ratio = calculate_sharpe_ratio(returns, risk_free_rate)
    print(f"Sharpe Ratio: {sharpe_ratio}")

if __name__ == "__main__":
    main()
```

README.md

```markdown
# Investment Analysis

This project performs an analysis of investment data to calculate the volatility and Sharpe ratio of an investment portfolio.

## Requirements

- Python 3.x
- pandas

## Usage

1. Clone the repository:

```
git clone <repository_url>
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the analysis:

```
python investment_analysis.py
```

## Data Format

The investment data should be provided in a CSV file named `investment_data.csv`, containing a column named "Price" representing the historical prices of the investment.
```

Note: The code assumes that the investment data is provided in a CSV file named `investment_data.csv`, and that the historical prices of the investment are stored in a column named "Price".
