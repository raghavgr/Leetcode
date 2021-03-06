import sys
"""
Say you have an array for which the ith element 
is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5
max. difference = 6-1 = 5 
(not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0
In this case, no transaction is done, i.e. max profit = 0.
"""
class Solution(object):
    """ 2 solutions """
    def maxProfit(self, prices):
        """
        One pass. O(n)
        :type prices: List[int]
        :rtype: int
        """
        lowest_price = sys.maxsize      # set it to maximum number
        largest_return = 0
        
        for i in prices:
            if i < lowest_price:
                lowest_price = i
            elif (i - lowest_price) > largest_return:
                largest_return = i - lowest_price
            
        return largest_return
    
    def maxProfit2(self, prices):
        """
        Brute Force O(n^2)
        :type prices: List[int]
        :rtype: int
        """
        q = -sys.maxsize - 1
        for i in range(len(prices) - 1):
            if prices[i] > prices[i + 1]:
                continue
            else:
                for j in range(i + 1, len(prices)):
                    if q < (prices[j] - prices[i]):
                        q = prices[j] - prices[i]
        if q > -sys.maxsize - 1:
            return q
        else:
            return 0

obj = Solution()
print(obj.maxProfit([7, 1, 5, 3, 6, 4]))