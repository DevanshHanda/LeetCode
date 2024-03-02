# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf1(n,i=[]):
            if n:
                leaf1(n.left)
                leaf1(n.right)
                if not (n.left or n.right):
                    i.append(n.val)
            return i
        def leaf2(n,i=[]):
            if n:
                leaf2(n.left)
                leaf2(n.right)
                if not (n.left or n.right):
                    i.append(n.val)
            return i
    
        k = leaf1(root1)
        m = leaf2(root2)
        
        if k==m:
            return True
        else:
            return False








