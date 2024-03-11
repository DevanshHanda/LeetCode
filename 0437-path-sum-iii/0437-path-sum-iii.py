# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def trav(n,p=[],c=[0]):
            if n:
                p.append(n.val)
                # print(p)
                for i in range(len(p)):
                    if sum(p[i:])==targetSum:
                        c[0]+=1
                trav(n.left)
                trav(n.right)
                p.pop()
            return c[0]
        return trav(root)