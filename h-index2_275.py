"""
Given an array of citations (each citation is a non-negative integer) of a researcher, 
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: 
"A scientist has index h if h of his/her N papers have at least h citations each, 
and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], 
which means the researcher has 5 papers in total 
and each of them had received 3, 0, 6, 1, 5 citations respectively. 
Since the researcher has 3 papers with at least 3 citations each 
and the remaining two with no more than 3 citations each, his h-index is 3.

What if the citations array is sorted in ascending order? Could you optimize your algorithm?

"""
class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        low = 0
        high = n - 1
        while low <= high:
            #print("high is " + str(high))
            #print("low is " + str(low))
            mid = (low + high) // 2
            if citations[mid] >= n - mid:
                high = mid - 1
            else:
                low = mid + 1
                #print("low got incremented to " + str(low) + " while high is "+ str(high))
        return n - low