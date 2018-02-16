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
    def mySqrt(self, num):
        """
        Binary search.
        :type x: int
        :rtype: int
        """
        if num <= 0: return 0
        if num == 1 or num == 2: return 1
        low = 0
        high = num - 1
        while low < high:
            mid = (low + high) // 2
            if mid**2 <= num and (mid + 1)**2 > num:
                return mid
            if mid**2 > num:
                high = mid
            if mid**2 < num:
                low = mid
    
    def mySqrt2(self, x):
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

obj = Solution()
print(obj.mySqrt(16))
print(obj.mySqrt(11))