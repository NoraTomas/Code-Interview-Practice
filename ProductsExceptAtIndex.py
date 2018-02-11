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
    products_before_index_list = []
    products_after_index_list = []

    for i,num in enumerate(ints):
        if (i == 0):
            products_before_index_list.append(1)

        else:
            temp = products_before_index_list[i-1]

            products_before_index_list.append(temp*num)
            print(products_before_index_list)





print(get_product_of_all_ints_except_at_index())