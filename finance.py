import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup

# apple = yf.Ticker("AAPL")
# apple_info=apple.info

# # print(apple)
# # # print('\n\n\n\n\n\n', apple_info)
# print(apple_info['country'])

# Using the history() method we can get the share price of the stock over a certain period of time. 
# Using the period parameter we can set how far back from the present to get data. 
# The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.

# apple_share_price_data = apple.history(period="max")
# print(apple_share_price_data.head())

#### apple_share_price_data.plot(x="Date", y="Open")
#doesn't work the plot


# amd=yf.Ticker('AMD')
# amd_info=amd.info
# print(amd_info['country'])
# print(amd_info['sector'])
# price_amd=amd.history(period='max')
# print(price_amd.head())


#---------------------
# url = "http://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

# data  = requests.get(url).text
# soup = BeautifulSoup(data, 'html.parser')
# netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# # First we isolate the body of the table which contains all the information
# # Then we loop through each row and find all the column values for each row
# for row in soup.find("tbody").find_all('tr'):
#     col = row.find_all("td")
#     date = col[0].text
#     Open = col[1].text
#     high = col[2].text
#     low = col[3].text
#     close = col[4].text
#     adj_close = col[5].text
#     volume = col[6].text
    
#     # Finally we append the data of each row to the table
#     netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    

#     print(netflix_data.head())

# #---------------------------
# #We can also use the pandas read_html function using the url
# read_html_pandas_data = pd.read_html(url)

# #---------------------------
# #Or we can convert the BeautifulSoup object to a string
# read_html_pandas_data_1 = pd.read_html(str(soup))

# netflix_dataframe = read_html_pandas_data[0]
# netflix_dataframe_1 = read_html_pandas_data_1[0]

# print('\n\n\n\n\n',netflix_dataframe.head())
# print('\n\n\n\n\n',netflix_dataframe_1.head())

#------------------
#task


url = 'http://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html'
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')
title_tag=soup.title
print('\n',title_tag)

amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", 'Adj Close',"Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)

# print(amazon_data.head())

#------ can bw that as well----
# amazon_data_1 = pd.read_html(str(soup))
# amazon_df = amazon_data_1[0]
# print(amazon_df.head())
#---------
# print(amazon_data.columns)

# print(amazon_data.size, '   size')
# print(amazon_data.shape, '   shape')
# print(len(amazon_data.index), ' len index')

#prints ;ast row in column 'open'
print(amazon_data.loc[len(amazon_data.index)-1]['Open'])
