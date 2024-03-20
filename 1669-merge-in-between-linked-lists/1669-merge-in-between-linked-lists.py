# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        h1 = list1
        for i in range(a-1):
            h1=h1.next
        newa = h1
        for i in range(a,b+2):
            h1=h1.next
        t = list2
        while t.next:
            t=t.next
        t.next = h1
        newa.next = list2
        return list1

