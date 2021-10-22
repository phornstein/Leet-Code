/**********************************************************************
9. Palindrome Number
Author: phornstein
Date: 20 October 2021

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.

Params:
    -231 <= x <= 231 - 1
*********************************************************************/

class Solution {
    public boolean isPalindrome(int x) {
        //this method will be written without using built in functions
        
        String xString = Integer.toString(x); //must strictly convert to string from int
        int xLength = xString.length();
        
        char[] ch = new char[xLength]; //arrays in Java are not dynamically sized
        //Note: we could just create a string directly instead of an array but the point of
        //this demo is to showcase arrays in other languages
        
        int j = 0; //we have to loop through the string to create char array...
        for (int i=xLength-1;i>=0;i--){ //might as well also reverse it while we do this...
            ch[i] = xString.charAt(j);
            j++;            
        }
        
        String xReversed = String.valueOf(ch);
        
        return xString.equals(xReversed);
    }
}

/****************************************************************************************
Runtime: 8 ms, faster than 60.95% of Java online submissions for Palindrome Number.
Memory Usage: 38.7 MB, less than 53.00% of Java online submissions for Palindrome Number. 
****************************************************************************************/