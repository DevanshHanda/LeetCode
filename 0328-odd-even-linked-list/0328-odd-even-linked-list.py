# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if  not head or not head.next or not head.next.next:
            return head

        odd_tail = ListNode(head.val)
        odd = head
        odd_head = odd_tail

        even_tail = ListNode(head.next.val)
        even = head.next
        even_head = even_tail

        while odd.next and even.next:
            odd = odd.next.next 
            even = even.next.next

            odd_tail.next = odd
            even_tail.next = even
            odd_tail = odd_tail.next
            even_tail = even_tail.next

        odd_tail.next = even_head
        return odd_head

