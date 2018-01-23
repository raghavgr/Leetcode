"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

Example 1
Input: [3,0,1]
Output: 2

Example 2
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. 
Could you implement it using only constant extra space complexity?
"""
class Solution:
    """ 3 solutions """
    def missingNumber(self, nums):
        """
        First solution. With O(len(nums)) complexity.
        :type nums: List[int]
        :rtype: int
        """
        print(str(len(nums)))
        ls = [True] * (len(nums) + 1)
        for i in range(len(nums)):
            ls[nums[i]] = False
        for i in range(len(ls)):
            if ls[i] == True:
                return i
    
    