""""
Given a roman numeral, convert it to an integer.

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

class Solution:
    def romanToInt(self, s) -> int:
        """
        Brute Force Approach
        
        Runtime: 52 ms, faster than 48.29% of Python3 online submissions for Roman to Integer.
        Memory Usage: 14.3 MB, less than 59.65% of Python3 online submissions for Roman to Integer.
        """
        roman = {'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000,
                'f':4,
                'n':9,
                'F':40,
                'N':90,
                'h':400,
                'H':900}

        for r in (('IV','f'),('IX','n'),('XL','F'),('XC','N'),('CD','h'),('CM','H')):
            s = s.replace(*r) # * unpacks tuple into two values for the replace functin

        out = 0
        for i in s:
            out += roman.get(i)

        return out

    def romanToIntZip(self,s) -> int:
        """
        Marginally more elegant solution with zip()

        Runtime: 62 ms, faster than 20.51% of Python3 online submissions for Roman to Integer.
        Memory Usage: 14.1 MB, less than 95.12% of Python3 online submissions for Roman to Integer.
        """
        roman = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000}

        values = [0] + [roman[c] for c in s[::-1]]

        total = 0
        for c, p in zip(values[1:], values):
            total = total - c if c < p else total + c

        return total