# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def postorder(root,l):
    if root:
        postorder(root.left,l)
        postorder(root.right,l)
        l.append(root.val)
    else:
        l.append('a')
    return l
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l1,l2=[],[]
        l1=postorder(p,l1)
        l2=postorder(q,l2)
        if l1 == l2: 
            return True
        else:
            return False
