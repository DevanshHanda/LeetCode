# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def trav(n,l=[]):
            if n:
                if val==n.val:
                    l.append(n)
                trav(n.right)
                trav(n.left)
            return l
        l=trav(root)
        if l:
            return l[0] 
        else:
            return None