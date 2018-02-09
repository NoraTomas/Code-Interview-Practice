"""
Write a function Write a function get_products_of_all_ints_except_at_index() that
takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

"""

from functools import reduce

ints = [1, 7, 3, 4]

result_list = []

def get_product_of_all_ints_except_at_index():
    for int in ints:
        result_list.append(multiply_list(ints)/int)



def multiply_list(numbers):
    product = 1

    for int in numbers:
        product = product*int

    return product

get_product_of_all_ints_except_at_index()
print(result_list)