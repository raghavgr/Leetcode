"""
Find the contiguous subarray within an array 
(containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

class Solution:
    def maxSubArray(self, nums):
        """
        Brute force solution to maximum subarray problem
        O(n^2)
        :type nums: List[int]
        :rtype: int
        """
        curr_max = nums[0]
        left = 0
        right = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum >= curr_max:
                    curr_max = sum
                    left = i
                    right = j
        return curr_max