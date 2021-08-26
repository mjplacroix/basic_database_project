# connect to the database, query, and return the results in a python script

import psycopg2
import config

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

cur.execute(r"""
            COPY stocks(stock, date, closing_price)
            FROM 'C:\Users\mlacroix_smartasset\data_project\tesla_prices.csv'
            DELIMITER ','
            CSV HEADER;
            """)
query_results = cur.fetchall()
print(query_results)


cur.execute("""
            SELECT s.stock, COUNT(s.stock)
            FROM stocks s
            GROUP BY 1;
            """)
query_results = cur.fetchall()
print(query_results)


cur.close()
conn.close()

