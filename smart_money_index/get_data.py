import yfinance as yf

msft = yf.Ticker("SPY")

# get stock info
print(msft.info)