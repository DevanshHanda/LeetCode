# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(n):
            if n:
                lheight = height(n.left)
                rheight = height(n.right)

                if lheight>rheight:
                    return lheight+1
                else:
                    return rheight+1
            return 0
        return height(root)


