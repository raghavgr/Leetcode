"""
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", 
a move consists of either replacing one occurrence of "XL" with "LX", 
or replacing one occurrence of "RX" with "XR". 
Given the starting string start and the ending string end, 
return True if and only if there exists a sequence of moves 
to transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
"""

class Solution:
    def canTransform(self, start, end):
        """
        Invariant method
        :type start: str
        :type end: str
        :rtype: bool
        """
        if not start.replace('X', '') == end.replace('X', ''):
            return False
        
        k = 0
        for i in range(len(start)):
            if start[i] == 'L':
                #print(i)
                while end[k] != 'L':
                    k = k + 1
                if i < k:
                    return False
                k += 1
        
        k = 0
        for i in range(len(start)):
            if start[i] == 'R':
                while end[k] != 'R':
                    k = k + 1
                if i > k:
                    return False
                k += 1
        
        return True