# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = [0]

        def compare(a,b):
            n = min(len(a),len(b))
            for i in range(n):
                if a[i]!=b[i]:
                    return len(a)+len(b)-2*i
            return max(len(a),len(b))-n


        def path_address(t,d={},s=''):
            if t:
                if t.left or t.right:
                    s+='l'
                    path_address(t.left,d,s)
                    s=s[:-1]
                    s+='r'
                    path_address(t.right,d,s)
                    s=s[:-1]
                else :
                    for i in d:
                        tc = compare(d[i],s)
                        if tc <= distance:
                            res[0]+=1
                    d[t]=s
                    s=s[:-1]
            return d
        d = path_address(root)
        # print(d)
        return res[0]
 
            
            