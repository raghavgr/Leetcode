"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? 
You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        My solution. O(n)
        :type nums: List[int]
        :rtype: List[int]
        """
        ls = set(nums)
        res = []
        for i in range(1, len(nums) + 1):
            if i not in ls:
                res.append(i)
        return res
    
    def findDisappearedNumbers2(self, nums):
        """
        O(n) and O(1) space solution
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
            if nums[abs(i) - 1] > 0:
                nums[abs(i) - 1] = -nums[abs(i) - 1]

        print(nums)
        return [i + 1 for i, n in enumerate(nums) if n > 0]

obj = Solution()
print(obj.findDisappearedNumbers([4,3,2,7,8,2,3,1]))