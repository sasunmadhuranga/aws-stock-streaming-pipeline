from pyathena import connect
import pandas as pd
import matplotlib.pyplot as plt

# Connect to Athena
conn = connect(s3_staging_dir='s3://stock-raw-data-bucket-1254/',
               region_name='us-east-1')

# Query
df = pd.read_sql("SELECT symbol, AVG(price) AS avg_price FROM stock_data GROUP BY symbol", conn)

# Plot
df.plot(kind='bar', x='symbol', y='avg_price', legend=False)
plt.title("Average Stock Price")
plt.ylabel("Price ($)")
plt.show()