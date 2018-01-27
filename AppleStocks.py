"""
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.

So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday
and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.
"""

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

def get_max_profit(stock_prices_yesterday):

    min_stock_price = stock_prices_yesterday[0]
    max_stock_price = stock_prices_yesterday[0]

    max_profit = 0

    for stock_price in stock_prices_yesterday:
        if stock_price < min_stock_price:
            min_stock_price = stock_price
            max_stock_price = 0

        elif stock_price > max_stock_price:
            max_stock_price = stock_price
            max_profit = max_stock_price - min_stock_price

    return max_profit



print(get_max_profit(stock_prices_yesterday))



