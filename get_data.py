import requests
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import config
import csv

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

df = pd.DataFrame(new_price_data, columns = ['stock','date','closing_price'])



# connect to postgresql database
conn = psycopg2.connect(host="localhost", 
                        port = 5432, 
                        database="dvdrental", 
                        user="postgres", 
                        password=config.postgresql_password)
cur = conn.cursor()
# first request
cur.execute("""
            SELECT s.stock, COUNT(s.stock)
            FROM stocks s
            GROUP BY 1;
            """)
query_results = cur.fetchall()
print(query_results)

# connect from client side to add data to table
engine = create_engine(f'postgresql://postgres:{config.postgresql_password}@localhost:5432/dvdrental')

# add data to table
df.to_sql('stocks', engine, if_exists='append', index=False)

# second request to confirm successful addition
cur.execute("""
            SELECT s.stock, COUNT(s.stock)
            FROM stocks s
            GROUP BY 1;
            """)
query_results = cur.fetchall()
print(query_results)

# close connection
cur.close()
conn.close()





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