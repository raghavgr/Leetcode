"""
Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
"""
class Solution:
    """ solution """
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(i for i in s if i.isalnum())  # remove special characters and spaces.
        s = s.lower()
        for i in range(len(s)//2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))