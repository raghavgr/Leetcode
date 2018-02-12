"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

class Solution:
    """ 2 solutions """
    def reverseString(self, s):
        """
        in-place reverse string algorithm
        i.e. another string is not used to store the result
        :type s: str
        :rtype: str
        """
        chars = list(s)
        for i in range(len(s) // 2):
            temp = chars[i]
            chars[i] = chars[len(s) - i - 1]
            chars[len(s) - i - 1] = temp
        return ''.join(chars)
    
    def reverseString_pythonic(self, s):
        """
        Reverse string using slicing
        :type s: str
        :rtype: str
        """
        return s[::-1]

obj = Solution()
print(obj.reverseString("hello")) # 'olleh'
print(obj.reverseString_pythonic("clara")) # 'aralc'