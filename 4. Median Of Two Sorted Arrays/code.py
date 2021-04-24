"""
4. Median Of Two Sorted Arrays
Author: phornstein
Date: 23 April 2021

Given two sorted arrays nums1 and nums2 of 
size m and n respectively, return the 
median of the two sorted arrays.

Params:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -10^6 <= nums1[i], nums2[i] <= 10^6
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        combined = nums1 + nums2
        combined.sort() #combine and sort lists
        size = len(combined) #get size once
        if size == 1: #if size is 1 the median is the first val
            return float(combined[0])
        
        if not size%2: #if size of list is even
            top = (size//2) #floor the size/2 which has a 1 start index
            bottom = top-1 #get bottom by subtracting 1 from top
            return (combined[top]+combined[bottom])/2.0
        else: 
            return combined[int(size/2)]

"""
Runtime: 92 ms, faster than 64.86% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.6 MB, less than 54.10% of Python3 online submissions for Median of Two Sorted Arrays.
"""