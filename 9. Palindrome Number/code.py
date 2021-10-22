"""
9. Palindrome Number
Author: phornstein
Date: 20 October 2021

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.

Params:
    -231 <= x <= 231 - 1
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst = list(str(x))
        lst_rev = lst.copy()
        #self.reverseList(lst_rev,0,len(lst)-1)
        self.reverseListRecursive(lst_rev,0,len(lst)-1)
        return lst==lst_rev



    def reverseList(self, A, start, end):
        '''Linear Algorithm to Reverse a List'''
        while start < end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1



    def reverseListRecursive(self,A, start, end):
        '''Recursive Algorithm to Reverse a List'''
        if start >= end:
            return
        A[start], A[end] = A[end], A[start]
        self.reverseListRecursive(A, start+1, end-1)

#### How I'd actually do it :) ####
class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst = list(str(x))
        lst_rev = lst.copy()
        lst_rev.reverse()
        return lst==lst_rev
