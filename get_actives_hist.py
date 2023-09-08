import yfinance as yf
from datetime import datetime

symbols = ["AAPL", "BA", "T", "MGM", "AMZN", "IBM", "TSLA", "GOOG"]
tickers = yf.Tickers(symbols)
end_date = datetime.now().strftime('%Y-%m-%d')
tickers_hist = tickers.history(period='max',end=end_date,interval='1m',)
tickers_hist = tickers_hist.stack(level=1).rename_axis(['Date', 'Ticker']).reset_index(level=1)
tickers_hist.to_csv('datasets\\actives_hist.csv')