"""
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842...,
 and since we want to return an integer, 
 the decimal part will be truncated.
"""
class Solution:
    def mySqrt(self, x):
        """
        Brute force. Got time limit exceeded.
        :type x: int
        :rtype: int
        """
        i = 1
        curr = 0
        while i <= x // i :
            if ((i+1)* (i+1)) > x:
                return i
            i += 1
        return curr
    