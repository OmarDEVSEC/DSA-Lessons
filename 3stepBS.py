# solve binary search problems in 3 steps. First lets go over the template

# Template for Binary Search algo

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

    # check if the middle element is the target
    if arr[mid] == target:
        return mid
    
    # if the target is less than the middle element, search in the left half
    elif target < arr[mid]:
        right = mid - 1
    
        # if the target is greater than the middle element, search in the right half
        # 
    else:
        left = mid + 1

    # taget element not found in the array
    return -1

# 3 parts of to adjust for Binary search template
# 1.) Set left and right pointers to boundaries of the search space
# 2.) Set return value to left or left -1
# 3.) Define the condition that will check if midpoint is valid (maybe a function)