class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brace_pairs = { '(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for char in s:
            if char in brace_pairs.keys():
                stack.append(char)
            elif char in brace_pairs.values():
                if len(stack) == 0 or char != brace_pairs[stack.pop()]:
                    return False
                else:
                    pass
        return len(stack) == 0

obj = Solution()
print(obj.isValid("{}["))
print(obj.isValid("(({}))(([{}]))"))