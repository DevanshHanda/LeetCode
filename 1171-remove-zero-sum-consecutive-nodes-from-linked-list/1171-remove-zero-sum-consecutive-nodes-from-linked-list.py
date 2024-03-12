# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#  below works but not efficient
# class Solution:
#     def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         t = head
#         l=[]
#         i,j=0,0
#         while t:
#             l.append(t.val)
#             t=t.next
#         while i < (len(l)):
#             j=i+1
#             while j <= (len(l)):
#                 # print(i,j)
#                 if sum(l[i:j])==0:
#                     l = l[:i]+l[j:]
#                     # print(l)
#                     i,j=0,i+1
#                 if i>len(l) or j>len(l):
#                     break
#                 j+=1
#             if i>len(l) or j>len(l)+1:
#                 break
#             i+=1
#         print(l)
#         while 0 in l:
#             l.remove(0)
#         i=1
#         try:
#             b = ListNode(l[0])
#         except:
#             return 
#         b = ListNode(l[0])
#         k = b
#         for i in range(1,len(l)):
#             b.next = ListNode(l[i])
#             b=b.next
#         return k

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sums = {0: dummy}
        current = head

        while current:
            prefix_sum += current.val
            if prefix_sum in prefix_sums:
                to_delete = prefix_sums[prefix_sum].next
                temp_sum = prefix_sum + to_delete.val
                while to_delete != current:
                    del prefix_sums[temp_sum]
                    to_delete = to_delete.next
                    temp_sum += to_delete.val
                prefix_sums[prefix_sum].next = current.next
            else:
                prefix_sums[prefix_sum] = current
            current = current.next

        return dummy.next


        




