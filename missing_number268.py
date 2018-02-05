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
        First solution. With O(n) complexity both time & space.
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
    
    def missingNumber2(self, nums):
        """
        Using the sequence sum formula. O(n), O(1) space
        :type nums: List[int]
        :rtype: int
        """
        total_sum = (len(nums)*(len(nums) + 1)) / 2
        sum_nums = sum(nums)
        return total_sum - sum_nums
    
    def missingNumber3(self, nums):
        """
        Using bit manipulation technique with XOR.
        Index	0	1	2	3
        Value	0	1	3	4
        missing = 4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4)
                = (4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2
                = 0∧0∧0∧0∧2
                = 2
        :type nums: List[int]
        :rtype: int
        """
        missing_num = len(nums)
        for i, num in enumerate(nums):
            missing_num ^= i ^ num
        return missing_num

