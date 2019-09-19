# Cryptocurrency-News-and-Prediction
A web app to display cryptocurrency news and forecast a cryptocurrency's price for the next day.

## Objective

The purpose of this web app is to grab cryptocurrency details from cryptocompare.com through an api and display them on the web application. 
Moreover a machine learning model will be used to predict the price of a cryptocurrency for the next day.

## Things tried

1. Demonstrated my knowledge of using API's by using the CryptoCompare API to grab cryptocurrency news, current price and the historical price of a given cryptocurrency.
2. Using bootstrap cards to display the news details cleanly.
3. Displaying the Current price, Highest price of the day, Lowest price of the day and the market cap of a few cryptocurrencies in a tabular form.
4. Using Holt Winter's method to predict the price for the next day.
5. Using Plotly to plot the trend of a given cryptocurrency.
6. Search bar to search for a cryptocurrency. If an unknown search term is entered, an error will be displayed.

### Home Page

When the home page loads, the table of cryptos and the news information comes up.

**Table of cryptos**

![Alt text](images/crypto-main.png?raw=true "Title")

**News Information**

![Alt text](images/crypto-news.png?raw=true "Title")

### Search Page

**Search for Crypto**

![Alt text](images/search-crypto.png?raw=true "Title")

**Searched Crypto's details**

![Alt text](images/crypto-head.png?raw=true "Title")

**Historical data of a crypto**

![Alt text](images/crypto-head.png?raw=true "Title")

**Error when a searched crypto is not found**

![Alt text](images/crypto-error.png?raw=true "Title")
