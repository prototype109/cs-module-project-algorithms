'''
Input: an integer
Returns: an integer
'''
# Understand
## input is an integer representing the number of cookies to be eaten
## output is an integer representing how many ways the number of cookies could be eaten
## given a number I must figure out all the premutations that the number can be transformed into additions of 1, 2, or 3
## there is a test for small input which goes up to 10 and big input that starts at 50
## seems like I only care about the number of ways the cookies can be eaten and not the output of the ways they can be eaten
## A successful premutation I think is when i've eaten all the cookies and there are no cookies left.
## Example
    ## 10 cookies
    ## 3, 3, 3 - 1 cookie left
    ## 2, 2, 2, 2 ,2 - 0 cookies left
    ## 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 - 0 cookies left (1's should always give zero cookies left)
    ## what I need to do with the remainder cookies I think I just run them through the function as a recursion I will eventually get a permutation
# Plan
## hint says I need to use recursion since I have premutations of a number
## base case has to be when it reaches 0 or less then I need to return and not count the last number if it made it negative
## I think I need a counter that counts every time a successful premutation is made, need to figure out what a successful premutation is
## I can divide the number and pass it's remainder for further reduction until I get 0

# n = 2, n = 0
# def eating_cookies(n, cache = {}):
#     # Your code here
#     i = 0

#     # if n is in the cache
#         # return what's in the cache
#     # else
#         # do expensive calculation and store result in cache
#     pass

# n = 3
def eating_cookies(n, arr = None):
    # Your code here
    # i = 0, i = 0
    count = 0

    if arr is None:
        arr = [0 for i in range(n + 1)]
    
    if arr[n] > 0:
        return arr[n]
    else:
        if n < 2:
            if n == 0:
                arr[0] = 1
            else:
                arr[0] = 1
                arr[1] = 1
        else:
            stop = 4 if n >= 4 else n + 1
            for i in range(1, stop):
                count += eating_cookies(n - i, arr)
                arr[n] = count
    return arr[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 0

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    num_cookies = 1

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    num_cookies = 2

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    num_cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    num_cookies = 4

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    num_cookies = 6

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    num_cookies = 7

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    num_cookies = 8

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    num_cookies = 9

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    num_cookies = 10

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
