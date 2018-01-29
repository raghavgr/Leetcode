"""
Find the contiguous subarray within an array 
(containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # print(len(nums))
        return self.maximum_subarray(nums, 0, (len(nums) - 1))[2]
    
    def maximum_subarray(self, arr, low, high):
        """
        Divide and conquer method of solving maximum subarray problem.
        :type arr: List[int]
        :type low, high: int
        :rtype: (int, int, int)
        """
        if high == low:
            #print(low)
            return (low, high, arr[low])
        mid = (low + high) // 2

        left = self.maximum_subarray(arr, low, mid)
        right = self.maximum_subarray(arr, mid+1, high)
        cross = self.maximum_crossing_subarray(arr, low, mid, high)

        if left[2] >= right[2] and left[2] >= cross[2]:
            return left
        elif right[2] >= left[2] and right[2] >= cross[2]:
            return right
        else:
            return cross

    def maximum_crossing_subarray(self, arr, low, mid, high):
        """
        A helper used to find if there is a contiguous subarray with the largest sum 
        of the array such that middle element of the array is part of it.
        :type arr: List[int]
        :type low, mid, high: int
        :rtype: (int, int, int)
        """
        left_sum = -9223372036854775808       # import sys, -sys.maxsize -1, lowest number
        sum = 0
        left_max = 0
        for i in range(mid, low-1, -1):
            sum += arr[i]
            if sum > left_sum:
                left_sum =sum
                left_max = i
        right_sum = -9223372036854775808
        sum = 0
        right_max = 0
        for i in range(mid + 1, high+1):
            sum += arr[i]
            if sum > right_sum:
                right_sum = sum
                right_max = i
        return (left_max, right_max, left_sum + right_sum)
    
    # def maxSubArray(self, nums):
    #     """
    #     Brute force solution to maximum subarray problem
    #     O(n^2)
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     curr_max = nums[0]
    #     left = 0
    #     right = 0
    #     for i in range(len(nums)):
    #         sum = 0
    #         for j in range(i, len(nums)):
    #             sum += nums[j]
    #             if sum >= curr_max:
    #                 curr_max = sum
    #                 left = i
    #                 right = j
    #     return curr_max

obj = Solution()
b_list = [-2,1,-3,4,-1,2,1,-5,4]
print(obj.maxSubArray([-2, -5, 6, -2, -3, 1, 5, -6]))
print(obj.maxSubArray(b_list))