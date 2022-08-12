import sqlalchemy
import yfinance as yf
import pandas as pd

tickers = pd.read_html(
    'https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average'
)[1]

tickers = tickers.Symbol.to_list()

df = pd.DataFrame()

for ticker in tickers:
    var = yf.Ticker(ticker).info
    frame = pd.DataFrame([var])

    df = df.append(frame)

engine = sqlalchemy.create_engine('sqlite:///Fundamentals.db')

subdf = df[['symbol', 'dividendYield', 'sector', 'shortRatio',
          'forwardPE','trailingPE']]

subdf.to_sql('Fundamentalstable', engine, index=False)
