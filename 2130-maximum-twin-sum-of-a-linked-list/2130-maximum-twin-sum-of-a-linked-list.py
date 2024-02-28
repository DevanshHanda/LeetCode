# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # e = ListNode()
        # h = ListNode()
        e = head
        l = []
        while e:
            l.append(e.val)
            # print(0)
            e=e.next
        n = len(l)
        s = [l[i]+l[n-1-i] for i in range(n//2)]
        return max(s)
