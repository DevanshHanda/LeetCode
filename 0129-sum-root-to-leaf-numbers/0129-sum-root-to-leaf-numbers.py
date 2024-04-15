# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def trav(n,l=[],sum=[0]):
            if n:
                l.append(n.val)
                trav(n.left)
                trav(n.right)                
                if not n.left and not n.right:
                    i=10**(len(l)-1)
                    for j in l:
                        sum[0]+=j*i
                        i=int(i/10)
                l.pop()
            return sum[0]
        return trav(root)


