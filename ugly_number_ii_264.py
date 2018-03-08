"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
"""
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num >= 2:
            if num % 2 == 0: num = num // 2
            elif num % 3 == 0: num = num // 3
            elif num % 5 == 0: num = num // 5
            else: return False
        return num == 1
    
    def nthUglyNumber1(self, n):
        initial = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
        primes = [7, 11]
        i = 13
        count = 10
        if n <= 10:
            return initial[n - 1]
        while count < n:
            if self.isUgly(i):
                count += 1
            i += 1
        return i - 1
    
    def nthUglyNumber_2(self, n):
        """
        Time Limit exceeded. 
        :type n: int
        :rtype: int
        """
        initial = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
        primes = [7, 11]
        i = 13
        count = 10
        if n <= 10:
            return initial[n - 1]
        while count < n:
            if (i % 2 == 0 or i%3 ==0 or i%5 ==0):
                primes_div = False
                for t in set(primes):
                    if i% t == 0:
                        primes_div = True
                if not primes_div:
                    count += 1
            else:
                for t in set(primes):
                    if i % t == 0:
                        continue
                    else:
                        primes.append(i)    
            i+=1

        return i-1