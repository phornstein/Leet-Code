"""
26. Remove Duplicates from Sorted Array
Author: phornstein
Date: 23 April 2021

Given a sorted array nums, remove the duplicates in-place such 
that each element appears only once and returns the new length.

Params: 
    0 <= nums.length <= 3 * 10^4
    -10^4 <= nums[i] <= 10^4
    nums is sorted in ascending order
Returns:
    len of new nums
"""
class Solution:
    def removeDuplicates(self, nums) -> int:
        if not len(nums): #check that list has values
            return 0
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                del nums[i]
            else:
                i+=1
        return i

"""
Runtime: 92 ms, faster than 40.96% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.7 MB, less than 94.12% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""