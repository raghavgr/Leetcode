class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        res = set()
        for i in range(len(nums)-2):
            start = i + 1
            end = len(nums) - 1
            #print("i is: " + str(i))
            while start < end:
                #print("start is: " + str(start) + ' end is: ' + str(end))
                t_sum = nums[i] + nums[start] + nums[end] # total sum
                if t_sum > 0:
                    end -= 1
                if t_sum < 0:
                    start += 1
                if(t_sum == 0):
                    res.add((nums[i], nums[start], nums[end]))
                    end -= 1
                    start += 1
        return list(res)

obj = Solution()
print(obj.threeSum([-1, 0, 1, 2, -1, -4])) # return 3