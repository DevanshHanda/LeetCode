# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         def height(n):
#             if n:
#                 return 1+max(height(n.left),height(n.right))
#             return 0
#         def diameter(n,i=[0]):
#             if n:
#                 diameter(n.left)
#                 diameter(n.right)
#                 left = height(n.left)
#                 right = height(n.right)
#                 if i[0]<left+right:
#                     i[0]=left+right
#                 return i[0]
        
#         return diameter(root)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        def diameter(root):
            if root is None:
                return -1

            lh=diameter(root.left)
            rh=diameter(root.right)
            ans[0]=max(ans[0],2+lh+rh)
            return 1+max(rh,lh)

        diameter(root)
        return ans[0]