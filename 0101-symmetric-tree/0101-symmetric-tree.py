# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        
        if not root.left or not root.right:
            return False
        
        def travpre1(n,p=[]):
            if n:
                p.append(n.val)
                travpre1(n.left)
                travpre1(n.right)
            else:
                p.append(None)
            return p
        def travin1(n,p1=[]):
            if n:
                travin1(n.left)
                p1.append(n.val)
                travin1(n.right)
            return p1
        def travpre(n,p=[]):
            if n:
                p.append(n.val)
                travpre(n.right)
                travpre(n.left)
            else:
                p.append(None)
            return p
        def travin(n,p1=[]):
            if n:
                travin(n.right)
                p1.append(n.val)
                travin(n.left)
            return p1

        a = travpre1(root.left)
        b = travpre(root.right)
        
        a1 = travin1(root.left)
        b1 = travin(root.right)

        # print(a)
        # print(b)
        # print(a1)
        # print(b1)
        if a==b and a1==b1:
            return True
        else:
            return False
        