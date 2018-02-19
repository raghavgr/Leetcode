"""
Given an integer, write a function to determine if it is a power of two.
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        i = n
        while i >= 2:
            if i % 2 == 0:
                i = i // 2
            else:
                return False
        return True

obj = Solution()
print(64)
print(obj.isPowerOfTwo(64))
print(23)
print(obj.isPowerOfTwo(23))