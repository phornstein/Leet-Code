"""
8. String to Integer (atoi)
Author: phornstein
Date 5 May 2021

Implement the myAtoi(string s) function, which converts 
a string to a 32-bit signed integer 
(similar to C/C++'s atoi function).

Params:
    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case), 
        digits (0-9), ' ', '+', '-', and '.'.
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ') #remove white spaces first
        if not len(s):
            return 0
        neg = False

        if (s[0] in ["-","+"] or not s[0].isdigit()):
            if s[0] == "-": #find negative signs
                neg = True
                s = s[1:]
            elif s[0] == "+": #treat positive signs
                s = s[1:]
            else: #if the first value is not a digit return 0
                return 0
            if not len(s):
                return 0
        if (s[0] in ["-","+"] or not s[0].isdigit()):
            return 0
        for ind,ch in enumerate(s):
            if not ch.isdigit():
                s = s[:ind]
                break
        out = int(s)*-1 if neg else int(s)
        if out < -2147483648: return -2147483648 
        if out > 2147483647: return 2147483647
        else: return out        
"""
Runtime: 24 ms, faster than 98.12% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14.2 MB, less than 56.64% of Python3 online submissions for String to Integer (atoi).
"""