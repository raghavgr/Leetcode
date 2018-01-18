"""
Given a non-negative integer num, 
repeatedly add all its digits 
until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. 
Since 2 has only one digit, return it.
"""
class Solution:
    """ Solution """
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while (num // 10 > 0):
            sum = 0
            while num > 0:
                sum += num % 10
                num = num // 10
            num = sum
        return num

    def addDigits_2(self, num):
        """
        Using some tricky mathematics
        :type num: int
        :rtype: int
        """
        return ((num - 1) % 9) + 1
