"""
You have a total of n coins that you want to form in a staircase shape, 
where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits 
within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        sum = 0
        i = 1
        while sum <= n and i < n:
            sum = sum + i
            count += 1
            i += 1
        #print(count)
        if n == 1 or n == 0:
            return n
        if n == 2:
            return 1
        if n == 3 or n == 4:
            return 2
        return count - 1
            
obj = Solution()
print(obj.arrangeCoins(8)) # return 3