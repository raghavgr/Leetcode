"""
Sort a linked list using insertion sort.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        newList = ListNode(0)
        newList.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:
                prev = newList   # newList.next.val is used below

                while prev.next.val < curr.next.val:
                    prev = prev.next

                temp = curr.next
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp
            else:
                curr = curr.next
        return newList.next