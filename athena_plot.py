from pyathena import connect
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


conn = connect(
    s3_staging_dir='s3://stock-raw-data-bucket-1254/',
    region_name='us-east-1'
)

query1 = """
SELECT 
    symbol,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    AVG(price) AS avg_price
FROM stock_data
GROUP BY symbol
ORDER BY avg_price DESC;
"""
df1 = pd.read_sql(query1, conn)
df1.plot(kind='bar', x='symbol', y=['min_price', 'avg_price', 'max_price'], figsize=(10,6))
plt.title("Stock Prices: Min, Avg, Max")
plt.ylabel("Price ($)")
plt.show()

query2 = """
SELECT 
    symbol,
    STDDEV(price) AS volatility
FROM stock_data
GROUP BY symbol
ORDER BY volatility DESC;
"""
df2 = pd.read_sql(query2, conn)
sns.barplot(x='volatility', y='symbol', data=df2, palette="coolwarm")
plt.title("Stock Price Volatility")
plt.xlabel("Standard Deviation ($)")
plt.show()

query3 = """
SELECT 
    symbol,
    date_trunc('hour', from_iso8601_timestamp(timestamp)) AS hour,
    AVG(price) AS avg_price
FROM stock_data
GROUP BY symbol, date_trunc('hour', from_iso8601_timestamp(timestamp))
ORDER BY hour;
"""
df3 = pd.read_sql(query3, conn)
plt.figure(figsize=(12,6))
for symbol in df3['symbol'].unique():
    df_symbol = df3[df3['symbol'] == symbol]
    plt.plot(df_symbol['hour'], df_symbol['avg_price'], label=symbol)
plt.legend()
plt.title("Hourly Average Price Trend")
plt.xlabel("Hour")
plt.ylabel("Price ($)")
plt.xticks(rotation=45)
plt.show()