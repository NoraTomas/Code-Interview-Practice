"""
Given a list of integers, find the highest product you can get from three of the integers

The input list_of_ints will always have at least three integers.

The list [8, 2, 5, 7, 3] (as a test list) will return 280 as the result

"""

list_of_ints = [3, 2, 5, 7, 8]
highest_integers_so_far = [1, 1, 1]


def highest_product_from_three_integers():
    result = 1

    for i,n in enumerate(list_of_ints):
        highest_integers_so_far.

    for i,n in enumerate(highest_integers_so_far):
        result *= n

    print(highest_integers_so_far)
    return result


print(highest_product_from_three_integers())


