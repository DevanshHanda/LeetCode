# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p=[]
        t = head
        while t:
            p.append(t.val)
            t=t.next
        if p==p[::-1]: return True
        else: return False