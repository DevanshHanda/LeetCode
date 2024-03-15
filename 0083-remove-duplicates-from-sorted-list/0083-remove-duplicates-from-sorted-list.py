# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        t = head
        while t.next:
            k=t
            try:
                while k.val==k.next.val:
                    k=k.next
                t.next = k.next
                t = t.next
            except:
                t.next = None
                return head
        return head


