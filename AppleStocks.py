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

    min_price = stock_prices_yesterday[0]

    max_profit = 0

    for current_price in stock_prices_yesterday:
        min_price = min(min_price, current_price)

        potential_profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)

    return max_profit



print(get_max_profit(stock_prices_yesterday))



