# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        t= head
        while(t):
            t = t.next
            l+=1
        print(l)
        print(l-n)
        if l == n:
            t = head
            t = t.next
            return t
        
        t= head
        for i in range(l-n-1):
            t = t.next
        if t.next:
            t.next = t.next.next

        return head
