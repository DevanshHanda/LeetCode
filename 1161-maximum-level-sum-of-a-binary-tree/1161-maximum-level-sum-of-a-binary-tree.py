# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def trav(n,l=[0],d={}):
            if n:
                if l[0] not in d:
                    d[l[0]]=n.val
                else:
                    d[l[0]]+=n.val
                l[0]+=1
                trav(n.right)
                trav(n.left)
                l[0]-=1
            return d
        t=trav(root)
        # print(t)
        n=max(list(t.values()))
        for i in t:
            if t[i]==n:
                return i+1
