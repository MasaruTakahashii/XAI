
```javascript
// Import the necessary libraries
const axios = require('axios');

// Function to get the cryptocurrency price from an API
async function getCryptoPrice(cryptoCurrency) {
  try {
    const response = await axios.get(`https://api.coinbase.com/v2/prices/${cryptoCurrency}-usd/buy`);
    return response.data.data.amount;
  } catch (error) {
    console.log(`Error fetching ${cryptoCurrency} price: ${error.message}`);
    return null;
  }
}

// Function to calculate the total value of a cryptocurrency portfolio
async function calculatePortfolioValue(portfolio) {
  let totalValue = 0;

  for (const crypto of Object.keys(portfolio)) {
    const price = await getCryptoPrice(crypto);
    if (price) {
      totalValue += price * portfolio[crypto];
    }
  }

  return totalValue;
}

// Example usage
const myCryptoPortfolio = {
  bitcoin: 2,
  ethereum: 5,
  litecoin: 10
};

calculatePortfolioValue(myCryptoPortfolio)
  .then(value => console.log(`Total value of portfolio: $${value}`))
  .catch(error => console.log(error));
```
