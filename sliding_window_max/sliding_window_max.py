'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# Understand
## the input is a list of integers as well as an integer k which is the sliding widnow size
## the output is a list of integers that are the max number of each window
## the window is the collection of numbers currently being looked at to find the max value in
## the window traverses along the main list until it reaches the end
## i will assume the window is always smaller or equal to the main list
# Plan
## probably going to need to have a list that has the current window i'm looking at
    ## maybe some sort of list that has a copy of what I am currently looking at by slicing it off the array
        ## and then I insert it back where I sliced it from then increment my slicing portions
        ## must loop and check if I have made it to the end of the array
def sliding_window_max(nums, k):
    # Your code here
    maxList = []
    i = 0
    tempList = nums[i:k]
    maxList.append(max(tempList))

    # print(f'tempArr: {tempArr} numsArr: {nums}')

    while k < len(nums):
        i += 1
        k += 1
        tempList = nums[i:k]
        maxList.append(max(tempList))
        # print(f'tempArr: {tempList} numsArr: {nums}')
    
    return maxList
        


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
