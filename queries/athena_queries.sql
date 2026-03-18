SELECT symbol, AVG(price)
FROM stock_data
GROUP BY symbol;