
# Automated Portfolio Rebalancing Algorithm in Python

```python
import pandas as pd

def rebalance_portfolio(current_portfolio, target_weights, market_prices):
    # Convert current portfolio and target weights to pandas DataFrame
    current_portfolio_df = pd.DataFrame(current_portfolio, columns=['Ticker', 'Quantity'])
    target_weights_df = pd.DataFrame(target_weights, columns=['Ticker', 'Weight'])

    # Merge current portfolio and target weights based on ticker symbol
    merged_df = pd.merge(current_portfolio_df, target_weights_df, on='Ticker', how='outer').fillna(0)

    # Calculate target quantity of each asset based on target weights and total portfolio value
    merged_df['Target Quantity'] = merged_df['Weight'] * merged_df['Total Portfolio Value'] / merged_df['Market Price']

    # Calculate quantity difference between current and target portfolio
    merged_df['Quantity Difference'] = merged_df['Target Quantity'] - merged_df['Quantity']

    # Filter out assets with no difference in quantities
    rebalancing_assets = merged_df[merged_df['Quantity Difference'] != 0]

    # Generate rebalancing orders
    rebalancing_orders = []
    for index, row in rebalancing_assets.iterrows():
        ticker = row['Ticker']
        quantity_difference = row['Quantity Difference']
        market_price = market_prices[ticker]

        if quantity_difference > 0:
            order_type = 'Buy'
        else:
            order_type = 'Sell'
            quantity_difference = abs(quantity_difference)

        rebalancing_orders.append({
            'Ticker': ticker,
            'Order Type': order_type,
            'Quantity Difference': quantity_difference,
            'Market Price': market_price
        })

    return rebalancing_orders


# Example usage
current_portfolio = [('AAPL', 10), ('AMZN', 5), ('GOOG', 7)]
target_weights = [('AAPL', 0.4), ('AMZN', 0.3), ('GOOG', 0.3)]
market_prices = {'AAPL': 150, 'AMZN': 3000, 'GOOG': 2000}

orders = rebalance_portfolio(current_portfolio, target_weights, market_prices)
for order in orders:
    print(order)
```

This algorithm automates the portfolio rebalancing process based on target weights and current market prices. It calculates the difference in quantities for each asset in the portfolio and generates the necessary buy or sell orders to rebalance the portfolio according to the target weights. The market prices are provided as a dictionary with ticker symbols as keys.

The example usage demonstrates how the `rebalance_portfolio` function can be used with a sample current portfolio, target weights, and market prices. The resulting rebalancing orders are printed to the console.
