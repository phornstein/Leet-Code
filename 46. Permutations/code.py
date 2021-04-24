"""
46. Permutations
Author: phornstein
Date: 23 April 2021

Given an array nums of distinct integers, return all 
the possible permutations. You can return the answer 
in any order.

Params:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
"""

class Solution:
    def permute(self, nums):
        num_len = len(nums) #get length of nums once
        # if lst is empty then there are no permutations
        if not num_len: #this is still necessary to solve with recursion
            return []
    
        # If there is only one element in lst then, only one permuatation is possible
        if num_len == 1:
            return [nums]

        ouput = []
        for i in range(num_len):
            m = nums[i]
            rem_lst = nums[:i] + nums[i+1:] #remove current value
            for p in self.permute(rem_lst): #keep removing values while getting all combos
                ouput.append([m] + p)
        return ouput

"""
Runtime: 32 ms, faster than 96.25% of Python3 online submissions for Permutations.
Memory Usage: 14.5 MB, less than 15.12% of Python3 online submissions for Permutations
"""