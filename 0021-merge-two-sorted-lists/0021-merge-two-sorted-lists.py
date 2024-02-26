# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = list1
        l=[]
        while t1:
            l.append(t1.val)
            t1=t1.next
        t2 = list2
        while t2:
            l.append(t2.val)
            t2=t2.next
        l.sort()
        print(l)
        n=ListNode()
        if len(l)==0:
            return list1
        n.val = l[0]
        if len(l)==1:
            return n
        t1 = ListNode(l[1])
        n.next = t1
        for i in range(2,len(l)):
            t2=ListNode(l[i])
            t1.next = t2
            t1=ListNode()
            t1 = t2
        print(80)
        return n

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         cur = dummy = ListNode()
#         while list1 and list2:               
#             if list1.val < list2.val:
#                 cur.next = list1
#                 list1, cur = list1.next, list1
#             else:
#                 cur.next = list2
#                 list2, cur = list2.next, list2
                
#         if list1 or list2:
#             cur.next = list1 if list1 else list2
            
#         return dummy.next

            
            


