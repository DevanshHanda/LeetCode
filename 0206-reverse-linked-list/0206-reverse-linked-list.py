# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        if not head.next.next:
            t = head.next
            t.next = head
            head.next = None
            return t
        c = head
        f = head.next        
        ff = head.next.next
        c.next = None
        while ff:
            f.next = c
            c = f
            f = ff
            ff = ff.next
        f.next = c
        return f


