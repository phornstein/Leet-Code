"""
47. Permutations II
Author: phornstein
Date: 23 April 2021

Given a collection of numbers, nums, that might 
contain duplicates, return all possible unique 
permutations in any order.

Params:
    1 <= nums.length <= 8
    -10 <= nums[i] <= 10
"""

class Solution:
    def permuteUnique(self, nums):
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
            for p in self.permuteUnique(rem_lst): #keep removing values while getting all combos
                perm = [m] + p
                if not perm in ouput: #check that combo is unique
                    ouput.append(perm)
        return ouput

"""
Runtime: 416 ms, faster than 17.71% of Python3 online submissions for Permutations II.
Memory Usage: 14.3 MB, less than 96.82% of Python3 online submissions for Permutations II.

This answer is substantially the same as mine for Permutations I; however, a check for uniqueness
is added to the end. This results in a lower memory solution that is slower. Speed can be achieved
by not recalcuating a non-unique permutation and simply filtering it at the end.
"""