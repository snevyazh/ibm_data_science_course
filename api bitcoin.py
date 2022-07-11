#pip install plotly
# pip install mplfinance

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id( id = 'bitcoin', vs_currency = 'usd', days = 30)
# print(bitcoin_data)
bitcoin_prices_data=bitcoin_data['prices']
data = pd.DataFrame(bitcoin_prices_data, columns= ['TimeStamp' , 'Price'])
print(data.head())

data['Date']=pd.to_datetime(data['TimeStamp'], unit='ms')
print(data.head())
candlestick_data=data.groupby(data.Date.dt.date).agg({'Price':['min', 'max', 'first', 'last']})
print(candlestick_data.head())
# fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
#                 open=candlestick_data['Price']['first'], 
#                 high=candlestick_data['Price']['max'],
#                 low=candlestick_data['Price']['min'], 
#                 close=candlestick_data['Price']['last'])
#                 ])

# fig.update_layout(xaxis_rangeslider_visible=False)

# fig.show()



