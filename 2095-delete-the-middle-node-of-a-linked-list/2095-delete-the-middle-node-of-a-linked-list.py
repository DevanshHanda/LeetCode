# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        l=[]
        n = head
        while n:
            l.append(n.val)
            n=n.next
            c+=1
        if c==1:
            return head.next
        t = head
        for i in range(1,c//2):
            t = t.next
        try:
            t.next = t.next.next
            return head
        except:
            t.next = None
            return head
