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
"""

class Solution:
    """ solution """
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        count = [0] * (n+1)
        for i in citations:
            if i > n:
                count[n] += 1
            else:
                count[i] += 1
        sum = 0
        i = n
        while i >= 0:
            sum += count[i]
            if sum >= i:
                return i
            i -= 1
        return 0


    def hIndex2(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0
        sorted_cit = sorted(citations, reverse = True) # O(n lg n)
        print(sorted_cit)
        i = 0
        while i < len(citations) and sorted_cit[i] >= (i + 1):
            i += 1
        return i
    
    

obj = Solution()
print(obj.hIndex([5, 8, 10, 4, 3]))