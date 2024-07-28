# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root,l=[]):
            if root:
                inorder(root.left)
                l.append([root.val,root])
                # if 
                inorder(root.right)
            return l
        
        # print(inorder(root))
        p=[]
        t = inorder(root)
        k = sorted(t,key = lambda x:x[0])
        for i in range(len(k)):
            if k[i][0]!=t[i][0]:
                k[i][1].val,t[i][1].val = t[i][1].val,k[i][1].val
                break


        




        