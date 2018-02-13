"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    sorted_arr = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            sorted_arr.append(nums1[i])
            i += 1
        else:
            sorted_arr.append(nums2[j])
            j += 1
    sorted_arr += nums1[i:]
    sorted_arr += nums2[j:]
    
    print(sorted_arr)
    n = len(sorted_arr)
    median = -100
    if n % 2 == 0:
        mid = n // 2
        median = (sorted_arr[mid - 1] + sorted_arr[mid]) / 2.0
    else:
        median = float(sorted_arr[len(sorted_arr) // 2])
    return median

print(findMedianSortedArrays([1, 3], [2, 4]))