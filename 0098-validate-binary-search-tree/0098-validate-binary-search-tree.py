# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
# #         self.right = right
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # print('hi',root.val)
        # if root.left:
        #     if root.left.val<root.val:
        #         if root.left.left or root.left.right:
        #             return True and self.isValidBST(root.left)
        #         else:
        #             return True
        #     else:
        #         return False
        # if root.right:
        #     if root.right.val>root.val:
        #         if root.right.right or root.right.left:
        #             return True and self.isValidBST(root.right)
        #         else:
        #             return True
        #     else:
        #         return False

        # return True

# class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     def check(root):
    #         if root.left or root.right:
    #             if root.left and root.right:
    #                 return check(root.left)<root.val<check(root.right)
    #             elif root.left:
    #                 print(check(root.left),root.val)
    #                 return check(root.left)<root.val
    #             elif root.right:
    #                 return root.val<check(root.right)
    #         else:
    #             # print(root.val)
    #             return root.val
            
    #     if not root.left and not root.right:
    #         return True
    #     print('going checker')
    #     return check(root)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inf = float('inf')

        def check(root,u,d):
            if not root:
                return True
            if d<root.val<u:
                return check(root.left,root.val,d) and check(root.right,u,root.val)
            else:
                return False

        return check(root,inf,-inf)




        
        