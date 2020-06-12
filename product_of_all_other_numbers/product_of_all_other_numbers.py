'''
Input: a List of integers
Returns: a List of integers
'''
# Understand
## given a list of ints as input
## output a list of ints that are products of the rest of the numbers in the list
    ## excluding the current number found in the index that i'm looking at
# Plan
## I think I will just multiply all the values together as the solution for every index and just divide the current indexes
    ## number so that I get everything but that index for every index and that should be good
from functools import reduce

def reduce_multiply_arr(arr):
    num = 1

    zero_index = []

    for index, x in enumerate(arr):
        if x == 0:
            zero_index.append(index)
        else:
            num *= x

    return (num, zero_index)

def product_of_all_other_numbers(arr):
    # Your code here
    original_arr = arr[:]
    multipliedNum, z_index = reduce_multiply_arr(arr)
    
    if z_index:
        arr = [0] * len(arr)

        for index in z_index:
            arr[index] = multipliedNum
    else:
        arr = [multipliedNum] * len(arr)

        for index, num in enumerate(original_arr):
            arr[index] = int(arr[index] / num)

    return arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
