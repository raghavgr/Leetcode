"""
Given a positive integer n, 
find the least number of perfect square numbers 
(for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, 
return 3 because 12 = 4 + 4 + 4; 

given n = 13, 
return 2 because 13 = 4 + 9.
"""

import math
import sys
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        max_val = int(math.sqrt(n))
        #print(max_val)
        dp = [sys.maxsize] * (n + 1)
        tt = [i for i in range(0, n)]
        #print(tt)
        for i in range(1, n + 1):
            for j in range(1, max_val + 1):
                if i == j*j:
                    dp[i] = 1             #dp[4] = 2*2
                elif i > j*j:
                    if dp[i] < dp[i - j*j] + 1:
                        #print("dp[i] is lower: " + str(dp[i]) + ",i is: " + str(i))
                        dp[i] = dp[i]
                    else:
                        #print(i)
                        #print(dp[i - j*j])
                        dp[i] = dp[i - j*j] + 1
            #print(dp)
        return dp[n]
    
    def numSquares_clean(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(2, int(math.sqrt(n)) + 1):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        return dp[n]

obj =Solution()
print(obj.numSquares(16))