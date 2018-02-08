"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        for i in range(len(s) // 2):
            temp = chars[i]
            chars[i] = chars[len(s) - i - 1]
            chars[len(s) - i - 1] = temp
        return ''.join(chars)

obj = Solution()
print(obj.reverseString("hello")) # 'olleh'