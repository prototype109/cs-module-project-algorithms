'''
Input: a List of integers
Returns: a List of integers
'''

# Understand
## input is a list of ints
## output is a list of ints where all 0's come after any other number in the list
## doesn't say list won't be empty
## has example where there are no 0's in the list
## list can have negative numbers
## expected output seems to be the number of elements that are on the left have of the list that are not 0's
## list can be all negative numbers
# Plan
## google a solution :)
## maybe I can sort the list then pop all the negative numbers just before the 0's start and append those numbers to the end of the list then reverse the list
## I could make an list of all 0's then look through the list with ints and add any number I find that isn't 0 to it <-- probably best time complexity
## can find 0's and pop them and append to end of list
    ## can use this solution with the sorting solution would just need to find the first 0 then start popping until I encounter a non-zero, but wouldn't work
        ## if the list is all negative numbers
## I could append a number that I find while going through the list that is non-zero to a new list and then and the remaining size of the list difference as zeros

##############################################################################

# Adding to an array solution - didn't work
# ## I could make an list of all 0's then look through the list with ints and add any number I find that isn't 0 to it <-- probably best time complexity

# Adding to an array solution (append to array)
# ## I could append a number that I find while going through the list that is non-zero to a new list and then and the remaining size of the list difference as zeros

def moving_zeroes(arr):
    # Your code here

    # create an list the size of the list with all 0's in it

    # loop through entire list:
        # if item i'm looking at is non-zero:
            # add it to the created list

    # return the created list

    ## First solution - didn't work cause i'm adding the numbers the same way they came in
    # non_zeros_first = [0] * len(arr)

    # for i in range(0, len(non_zeros_first)):
    #     if arr[i] != 0:
    #         non_zeros_first[i] = arr[i]

    # return non_zeros_first

    if len(arr) == 0:
        return []

    non_zeros_first = []

    for i in range(0, len(arr)):
        if arr[i] != 0:
            non_zeros_first.append(arr[i])
    # [0] * 0 = []
    # [1] + [] = [1]
    return non_zeros_first + ([0] * (len(arr) - len(non_zeros_first)))



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

# Review - 1
## my first solution is just putting the numbers back in the same order because I am adding to it in the same way :(
## going to append it instead and not create predefinded space for the array, makes worse space complexity though

# Review - 2 
## solution works, it passes all the test I don't know what scenarios I have not considered but I have considered if the list is empty
    ## because the problem never stated that the list input would be empty
    ## I guess I could have considered if the list was not ints but the problem specifically said ints
## space complexity: O(n) because I needed another array the size of the input array
## time complexity: O(n) because 