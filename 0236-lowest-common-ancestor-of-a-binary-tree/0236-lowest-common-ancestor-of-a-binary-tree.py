# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        global y
        y = None  # Initialize y to None
        
        def trav(n, s, p=[]):
            global y  # Accessing global variable y
            if n:
                if n.val == s:
                    y = p[:]  # Assign a copy of p to y
                    return p
                p.append(n.val)
                # print(p)
                trav(n.left, s, p)
                trav(n.right, s, p)
                p.pop()
            return p

        trav(root, p.val)
        # print(y, p.val)
        yp = y[:]
        y = None

        trav(root, q.val)
        # print(y, q.val)
        yq = y[:]

        if p.val in yq:
            return p
        if q.val in yp:
            return q

        t = list(set(yp)&set(yq))
        # print(yp,yq,t)
        # i = list(t)[-1]
        i = t[0]
        if len(t)!=1:
            while len(t)!=1:
                for j in yp:
                    if j in t:
                        t.remove(j)
                        break 
        i=t[0]
        # print(i)
        global g
        g = None
        def find(n,s):
            global g
            if n:
                # print(n.val,s)
                if n.val==s:
                    g=n
                    return n
                t = find(n.left,s)
                t = find(n.right,s)
        find(root,i)
        return g
            

       