# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    # # Print nodes at a current level
    #     def printCurrentLevel(root, level,l=[]):
    #         if root is None:
    #             return
    #         if level == 1:
    #             l.append(root.val)
    #             print(root.val,end=' ')
    #         elif level > 1:
    #             printCurrentLevel(root.right, level - 1)
    #             printCurrentLevel(root.left, level - 1)
    #         return l

    # # Compute the height of a tree--the number of nodes
    # # along the longest path from the root node down to
    # # the farthest leaf node
    #     def height(node):
    #         if node is None:
    #             return 0
    #         else:

    #             # Compute the height of each subtree
    #             lheight = height(node.left)
    #             rheight = height(node.right)

    #             # Use the larger one
    #             if lheight > rheight:
    #                 return lheight + 1
    #             else:
    #                 return rheight + 1

    #     h = height(root)
    #     # print(h)
    #     l=[]
    #     for i in range(1, h + 1):
    #         l+=printCurrentLevel(root, i)
        
    #     return l[-1]
    def __init__(self):
        self.res = [0] * 2

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 1)
        return self.res[1]

    def dfs(self, node, depth):
        if not node:
            return

        if depth > self.res[0]:
            self.res[0] = depth
            self.res[1] = node.val
        
        self.dfs(node.left, depth+1)
        self.dfs(node.right, depth+1)
