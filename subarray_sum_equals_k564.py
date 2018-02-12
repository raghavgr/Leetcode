"""
Given an array of integers and an integer k, 
you need to find the total number of 
continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
"""
class Solution:
    def subarraySum2(self, nums, k):
        """
        Brute force, O(n^2)
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = [0] * (len(nums) + 1)
        print(len(sums))
        counter = 0
        for i in range(1, len(nums) + 1):
            sums[i] = (sums[i-1]  + nums[i-1])
        print(sums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)+1):
                if (sums[j] - sums[i] == k):
                    counter+=1
        #counter = 7
        return counter
    
    def subarraySum(self, nums, k):
        """
        Using a dictionary. O(N)
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {0: 1}
        total, res = 0, 0
        for i in range(len(nums)):
            total += nums[i]
            # print(nums[i])
            # print("total is: " + str(total))
            # print("total - k: " + str(total - k))
            res += count.get(total - k, 0)
            # print("res is: " + str(res))
            count[total] = count.get(total, 0) + 1
            # print(count)
        # print(count)
        return res

obj = Solution()
# nums = [1, 3, 0, 4, 2, 2, 5, -1, 6, -2, 1]
# k = 4
print(obj.subarraySum([1, 3, 0, 4, 2, 2, 5, -1, 6, -2, 1], 4))
