import math
class Solution:
    """ Solution """
    def countPrimes(self, n):
        """
        O(N) runtime, O(N) space
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        A = [True] * n
        for i in range(2, int(n ** 0.5) + 1):
            if A[i]:
                for i in range(i ** 2, n, i):
                    A[i] = False
        count = 0
        for i in range(len(A)):
            if A[i]:
                count +=1 
        return count - 2  # removed 0, 1 as they aren't primes

    def countPrimes2(self, n):
        """
        O(n^2)
        :type n: int
        :rtype: int
        """
        count = 0
        i = 2
        while i < n:
            if self.isPrime(i):
                count += 1
            i += 1
        return count
        
    def isPrime(self, num):
        if num== 2 or num == 3: 
            return True
        elif num%2==0 or num<2: 
            return False
        else:
            for i in range(3, int(math.sqrt(num)) + 1, 2):    # only odd numbers
                if num % i == 0:
                    return False

        return True