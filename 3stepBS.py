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


# More practice :)

# 1. left = 0, right = len(nums)
# 2. return left
# 3. use arr[mid] > arr[mid+1]

class Solution:
    def findPeakElement(self, nums:List[int]) -> int:
        # Edge case: if only one element, it's a peak
        if len(nums) == 1:
            return 0

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r-l) //2

            if nums[mid] > nums [mid + 1]:
                r = mid
            else:
                l = mid + 1
        
        return l # return needs to be outside of the loop, now the leetcode
    
    # problem works perfectly.