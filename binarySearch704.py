# # Leetcode problem 704: Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) //2 #Initilize/calculate the mid of the arr
            if nums[mid] == target:  #Check if target is mid of arr
                return mid
            elif target < nums[mid]:  # Check if taget is in the left side of the arr
                right = mid - 1
            else:
                left = mid + 1

            return - 1    