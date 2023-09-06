
```javascript
// Ethereum Smart Contract for Tokenized Assets

// Import required modules
const Web3 = require('web3');
const fs = require('fs');

// Define contract ABI
const contractABI = JSON.parse(fs.readFileSync('contractABI.json'));

// Initialize Web3
const web3 = new Web3('http://localhost:8545');

// Set default account for transactions
web3.eth.defaultAccount = web3.eth.accounts[0];

// Create instance of the contract
const contractInstance = new web3.eth.Contract(contractABI, '0x123456789abcdef');

// Define function to tokenize an asset
async function tokenizeAsset(assetId, owner, value) {
  try {
    // Validate inputs
    if (!assetId || !owner || !value) {
      throw new Error('Invalid input parameters');
    }

    // Tokenize asset
    const result = await contractInstance.methods.tokenizeAsset(assetId, owner, value).send();

    // Return transaction result
    return result;
  } catch (error) {
    console.error('Error tokenizing asset:', error);
  }
}

// Define function to transfer tokens
async function transferTokens(tokenId, to, value) {
  try {
    // Validate inputs
    if (!tokenId || !to || !value) {
      throw new Error('Invalid input parameters');
    }

    // Transfer tokens
    const result = await contractInstance.methods.transferTokens(tokenId, to, value).send();

    // Return transaction result
    return result;
  } catch (error) {
    console.error('Error transferring tokens:', error);
  }
}

// Define function to get token balance
async function getTokenBalance(tokenId, account) {
  try {
    // Validate inputs
    if (!tokenId || !account) {
      throw new Error('Invalid input parameters');
    }

    // Get token balance
    const balance = await contractInstance.methods.getTokenBalance(tokenId, account).call();

    // Return token balance
    return balance;
  } catch (error) {
    console.error('Error getting token balance:', error);
  }
}

// Export functions
module.exports = {
  tokenizeAsset,
  transferTokens,
  getTokenBalance,
};
```

contractABI.json

```json
[
  {
    "constant": false,
    "inputs": [
      {
        "name": "assetId",
        "type": "string"
      },
      {
        "name": "owner",
        "type": "address"
      },
      {
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "tokenizeAsset",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "name": "tokenId",
        "type": "uint256"
      },
      {
        "name": "to",
        "type": "address"
      },
      {
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "transferTokens",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "name": "tokenId",
        "type": "uint256"
      },
      {
        "name": "account",
        "type": "address"
      }
    ],
    "name": "getTokenBalance",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  }
]
```
