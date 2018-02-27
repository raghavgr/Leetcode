"""
You are given coins of different denominations and a 
total amount of money amount. Write a function to compute the 
fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

"""
class Solution(object):
    def coinChange2(self, coins, amount):
        """
        This solution and it's helper function were not accepted
        by leetcode judge.
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        minCoins, coinsUsed = self.dpMakeChange(coins, amount, [0]*(amount + 1))
        remaining = 0
        output = minCoins[amount]
        i = len(coinsUsed) - 1
        while i > 0:
            #print(coinsUsed[i])
            if remaining == amount:
                break
            if remaining > amount:
                output = -1
            remaining += coinsUsed[i]
            i = i - 1
        return output
            
    
    def dpMakeChange(self, coinValList, change, minCoins):
        """
        Dynamic programming version
        Returns optimal value but not the solution
        """
        
        coinsUsed = [0]*(change + 1)
        for cents in range(change + 1):
            coinCount = cents
            newCoin = 1
            for j in [c for c in coinValList if c <= change]:
                if minCoins[cents - j] + 1 < coinCount:
                    coinCount = minCoins[cents - j] + 1
                    newCoin = j
            minCoins[cents] = coinCount
            coinsUsed[cents] = newCoin
            #print(minCoins)
        print(coinsUsed)
        return (minCoins, coinsUsed)
        