# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        t = head
        l=[0]
        while t:
            l[-1]=t
            t=t.next
            l.append(0)
        l=l[:-1]
        n = len(l)-1

        if len(l)%2==0:
            c=len(l)//2
            for i in range(c-1):
                # print('connection ',i,'->',n-i,'->',i+1)
                # if i==n-i:
                #     # odd number
                #     # print('connection ',i,'->','None')
                #     l[i].next=None
                #     break
                # if n-i==i+1:
                #     # even number
                #     # print('connection ',i,'->',n-i,'->','None')
                #     l[i].next=l[n-i]
                #     l[n-i].next=None
                #     break
                # print(l[i].val,l[n-i].val,l[i+1].val)
                l[i].next = l[n-i]
                l[n-i].next = l[i+1]
            i = int(c - 1)
            l[i].next=l[n-i]
            l[n-i].next=None
        else:
            # c=len(l)//2+1
            c=len(l)//2
            for i in range(c):
                # print('connection ',i,'->',n-i,'->',i+1)
                # if i==n-i:
                #     # odd number
                #     # print('connection ',i,'->','None')
                #     l[i].next=None
                #     break
                # if n-i==i+1:
                #     # even number
                #     # print('connection ',i,'->',n-i,'->','None')
                #     l[i].next=l[n-i]
                #     l[n-i].next=None
                #     break
                # print(l[i].val,l[n-i].val,l[i+1].val)
                l[i].next = l[n-i]
                l[n-i].next = l[i+1]
            l[c].next=None
            
            # print(l)

        # for i in range(c // 2):
        #     l[i].next = l[c - i - 1]
        #     l[c - i - 1].next = l[i + 1]
        #     print(i,c-i-1,i+1)
    
        # if c % 2 == 1:
        #     print(c//2)
        #     l[c // 2].next = None
# ------------------------
# i = n/2  : odd number end
# i = n/2 -1 : even number end
        




            

        