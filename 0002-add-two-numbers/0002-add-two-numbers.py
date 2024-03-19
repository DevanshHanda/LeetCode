# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t=l1
        k1=''
        while t:
            k1+=str(t.val)
            t=t.next
        k1=int(k1[::-1])
        t=l2
        k2=''
        while t:
            k2+=str(t.val)
            t=t.next
        k2=int(k2[::-1])
        k3=str(k2+k1)[::-1]
        t = ListNode(k3[0])
        h = t
        for i in range(1,len(k3)):
            t1 = ListNode(k3[i])
            t.next = t1
            t=t1
        return h
        

