import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

tesla=yf.Ticker('TSLA')
print (tesla)
tesla_data = tesla.history(period='max')
tesla_data.reset_index(inplace=True)
print(tesla_data.head())


url='http://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'
html_data=requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')


all_tables = soup.find_all('table', attrs={'class': 'historical_data_table table'})

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

# for table in all_tables:
#     if table.find('th').getText().startswith("Tesla Quarterly Revenue"):
#         for row in table.find_all("tr"):
#             col = row.find_all("td")  
#             if len(col) == 2: 
#                 date = col[0].text
#                 revenue = col[1].text.replace('$', '').replace(',', '')
#                 tesla_revenue = tesla_revenue.append({"Date": date, "Revenue": revenue}, ignore_index=True)
#-------------
#can be this one
for row in soup.find_all('tbody')[1].find_all('tr'):
    col=row.find_all('td')
    date=col[0].text
    revenue=col[1].text.replace('$','').replace(',','')
    tesla_revenue = tesla_revenue.append({"Date": date, "Revenue": revenue}, ignore_index=True)

tesla_revenue.dropna(inplace=True)    
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
print(tesla_revenue.tail(5))
# tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
# tesla_revenue.dropna(inplace=True)

# tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
# make_graph(tesla_data, tesla_revenue, 'Tesla')




#------------------------
# url='http://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
# html_data=requests.get(url).text
# soup = BeautifulSoup(html_data, 'html.parser')
# gamestop=yf.Ticker('GME')
# gme_data=gamestop.history(period='max')
# tables = soup.find_all("tbody")[1]
# gme_revenue = pd.DataFrame(columns=['Data','Revenue'])
# for row in tables.find_all('tr'):
#     col=row.find_all('td')
#     if col != []:
#         date = col[0].text
#         revenue=col[1].text
#         gme_revenue=gme_revenue.append({'Date':date, 'Revenue':revenue}, ignore_index=True)
# print(gme_revenue)
# gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")
# gme_revenue.dropna(inplace=True)
# gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

# print(gme_revenue)
#print(gme_revenue)
#make_graph(gme_data, gme_revenue, 'Tesla')
# print(gme_revenue.tail(5))
#----------


