"""
Given an array of integers, every element appears twice except for one.
Find that single one.
"""
class Solution:
    def singleNumber(self, nums):
        """
        Using XOR logic.
        a ^ a = 0
        but a ^ a ^ b = b, the missing number
        :type nums: List[int]
        :rtype: int
        """
        a_xor = 0
        for i in nums:
            a_xor = a_xor ^ i
        return a_xor

    def singleNumber2(self, nums):
        """
        O(nlgn), sort list first and then loop over the array
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        i = 0
        nums2 = sorted(nums)
        print(nums2)
        while i < len(nums2) - 1:
            if nums2[i] != nums2[i + 1]:
                return nums2[i]
            else:
                i += 2
        return nums2[-1]                    # if the unique number is largest element of the sorted array