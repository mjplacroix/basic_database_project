import requests
import pandas as pd
import psycopg2
import config

# set list of stocks to request previous day history on
stock_list = ['twtr', 'nflx', 'tsla', 'sq', 'arkq']

# empty list to add new data to from each request - should I have column titles for adding to sql database?
new_price_data = []

# for loop to iterate through each one
for stock in stock_list:
    # api string to insert in each stock ticker
    previous_day_data = requests.get(f"https://sandbox.iexapis.com/stable/stock/{stock}/previous?token={config.sandbox_api}")
    # set equal to to variable - transform into list
    data = previous_day_data.json()
    individual_data = [data['symbol'], data['date'], data['close']]
    # add list to empty list above
    new_price_data.append(individual_data)

print(new_price_data)

# convert full list to dataframe

# dataframe to csv and save?

# open connection to local postgresql database 

# load new daily data into database

# query for last week of data to confirm upload

# close connection

# try to automate this entire script to auto run Tuesday-Saturday mornings for request & upload previous day's data


"""
response = requests.get("https://sandbox.iexapis.com/stable/stock/sq/chart/1y?token=Tsk_5f6e91e3214f444d8cbd93e241061fbc")

stock_list = []
for stock in response.json():
    day_list = [stock['symbol'], stock['date'], stock['close']]
    stock_list.append(day_list)

df = pd.DataFrame(stock_list, columns =['Stock', 'Date', 'Closing Price'])

df.to_csv('sq_prices.csv') 

"""

# print(response.status_code) 
# print(response.json())
# print('')