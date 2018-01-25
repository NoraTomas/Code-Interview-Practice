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

    max_profit = 0

    for outer_price in range(len(stock_prices_yesterday)):
        for inner_price in range(outer_price+1, len(stock_prices_yesterday)):

            print("Outer price: " + str(outer_price))
            print("Inner price: " + str(inner_price))

            earlier_price = stock_prices_yesterday[outer_price]
            later_price = stock_prices_yesterday[inner_price]

            potential_max_profit = later_price - earlier_price

            max_profit = max(max_profit, potential_max_profit)

    return max_profit


print(get_max_profit(stock_prices_yesterday))



