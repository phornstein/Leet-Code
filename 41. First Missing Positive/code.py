"""
41. First Missing Positive
Author: phornstein
Date: 23 April 2021

Given an unsorted integer array nums, find 
the smallest missing positive integer.

Params:
    1 <= nums.length <= 300
    -231 <= nums[i] <= 231 - 1
"""

class Solution:
    def firstMissingPositive(self, nums) -> int:
        nums.sort() #sort nums
        nums = [n for n in nums if n > 0] #remove negatives
        if not len(nums): #if no nums left after removing negatives
            return 1 #then first missing is 1
        if nums[0] > 1:
            return 1 #if the first digit is >1 the first missing is 1

        for i in range(len(nums)-1):
            if (nums[i+1] - nums[i]) > 1: #if diff is greater than 1 a num is missing
                return nums[i] + 1
        return nums[-1] + 1 #if no missing digit the first missing is the last digit plus 1

"""
Runtime: 20 ms, faster than 99.86% of Python3 online submissions for First Missing Positive.
Memory Usage: 14.4 MB, less than 14.50% of Python3 online submissions for First Missing Positive.
"""