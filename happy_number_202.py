"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, 
replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""
class Solution:
    """ Solution """
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numbers_seen = set()
        while True:
            if n not in numbers_seen:
                numbers_seen.add(n)
                n = sum([int(x)*int(x) for x in str(n)])
                if n == 1:
                    return True
            else:
                return False
    def isHappy2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        
        numbers_seen = set()
        while True:
            if n not in numbers_seen and n != 1:
                numbers_seen.add(n)
                sum = 0
                if n < 10:
                    n = n * n
                while n > 0:
                    sum +=  (n%10) * (n%10)
                    n = n // 10
                if sum == 1:
                    return True
                elif sum in numbers_seen:
                    return False
                else:
                    n = sum
                    
            else:
                return False

obj = Solution()
print(obj.isHappy(19))
print(obj.isHappy(7))
print(obj.isHappy2(68))