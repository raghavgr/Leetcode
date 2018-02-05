"""
Given a non-negative integer,
you could swap two digits at most once to get the maximum valued number.
Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
"""
class Solution:
    """
    solution
    """
    def maximum_swap1(self, num):
        """
        Brute force approach. 
        O(n^3)
        """
        A = list(str(num))
        ans = A[:]
        for i in range(0, len(A)):
            for j in range(i + 1, len(A)):
                A[i], A[j] = A[j], A[i]
                if A > ans: ans = A[:]
                A[i], A[j] = A[j], A[i]
        return int("".join(ans))

    def maximum_swap2(self, num):
        """
        Greedy approach to solving the problem
        """
        A = [int(d) for d in str(num)]
        last = {x: i for i, x in enumerate(A)}
        for i in range(len(A)):
            for j in range(9, A[i], -1):
                # here we loop through last dictionary
                # see where the index of a greater value is smaller
                # than a previous value. start from the end, at 9.
                # If there is one, swap and return.
                # O(N)

                """
                debug statements
                # print("j is: " + str(j))
                # print("last.get is: "+ str(last.get(j)))
                # print(i)
                """
                if j in last and last.get(j) > i:
                    A[i], A[last[j]] = A[last[j]], A[i]
                    return int("".join(map(str, A)))
        return num

obj = Solution()
print(obj.maximum_swap2(10973))
print(obj.maximum_swap2(2736))