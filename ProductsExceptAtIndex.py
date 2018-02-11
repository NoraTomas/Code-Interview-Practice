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



def get_product_of_all_ints_except_at_index():
    result_list = []
    temp = 1

    for i, outer in enumerate(ints):
        for j, inner in enumerate(ints):
            if not i == j:
                temp *= inner

        result_list.append(temp)
        temp = 1

    return result_list

print(get_product_of_all_ints_except_at_index())