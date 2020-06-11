'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# Understand
## takes in a list of ints
## list can be any size but needs at least one number that has no duplicate so minimum size of one
## returns the integer that has no duplicate in the list
## the output should be a single integer
## can return negative and positive numbers
## I'm not sure if this list of ints is in order
# Plan
## since I don't know if the list is in order I may want to sort it
#### this will help me find the non duplicate number easier as it will be surrounded by duplicates
## there might be a python library that helps me find non duplicate things in lists *shrugs*
## maybe I can use regex on this list, but I would need to turn the values into strings first to use regex
## google a way in python to find duplicate items in a list :)

####################################################################

# Counter solution
# https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them

# import collections counter, can be used to turn a list into a dictionary with a count of unique items in it

import collections

def single_number(arr):
    # Your code here

    # loop through arr:
        # if the touple that is obtain from calling Collections.Counter() on the arr count is one then we 
            # return that number

    for item, count in collections.Counter(arr).items():
        if count == 1:
            return item


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

# Review
## the solution looks clean but needed a library imported to work
## I think this would work on all cases