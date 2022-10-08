-- Question: Given table Stocks with primary key 'stock_name' and 'operation_day' and columns 'operation' and 'price'.
-- 'Operation' column is an ENUM of type 'Sell' and 'Buy'.
-- Each row indicates the stock which stock_name had an operation on the day operation_day with the price.
-- Guaranteed that each 'Sell' operation for a stock has a
-- corresponding 'Buy' operation in a previous day, and vice versa.
-- Write SQL query to report Capital gain/loss for each stock (Total gain or loss after buying and selling stock).

SELECT
    stock_name,
    SUM(CASE WHEN operation = 'Sell' THEN price ELSE 0 END) - SUM(CASE WHEN operation = 'Buy' THEN price ELSE 0 END)
    AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
