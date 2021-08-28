# connect to the database, query, and return the results in a python script

import psycopg2
import config
from sqlalchemy import create_engine
import pandas as pd

conn = psycopg2.connect(host="localhost", 
                        port = 5432, 
                        database="dvdrental", 
                        user="postgres", 
                        password=config.postgresql_password)

cur = conn.cursor()

cur.execute("""
            SELECT s.stock, COUNT(s.stock)
            FROM stocks s
            GROUP BY 1;
            """)
query_results = cur.fetchall()
print(query_results)

df = pd.read_csv(r'C:\Users\mlacroix_smartasset\data_project\tesla_prices.csv')
print(df.head())
print(df.shape)
df.reset_index()

engine = create_engine(f'postgresql://postgres:{config.postgresql_password}@localhost:5432/dvdrental')

df.to_sql('stocks', engine, if_exists='append', index=False)

# # data that wasn't executing due to permissions on the server side
# cur.execute(r"""
#             COPY stocks(stock, date, closing_price)
#             FROM 'C:\Users\mlacroix_smartasset\data_project\tesla_prices.csv'
#             DELIMITER ','
#             CSV HEADER;
#             """)
# query_results = cur.fetchall()
# print(query_results)


cur.execute("""
            SELECT s.stock, COUNT(s.stock)
            FROM stocks s
            GROUP BY 1;
            """)
query_results = cur.fetchall()
print(query_results)


cur.close()
conn.close()

