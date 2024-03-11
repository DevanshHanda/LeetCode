# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         # for a dynamic list which keeps all the elements as called
#         def trav(n,p=[],c=[0]):
#             if n:
#                 # print("inside calls")
#                 p.append(n.val)
#                 # This part is for keeping count alone
#                 if max(p)==p[-1]:
#                     c[0]+=1
#                 # print('l_call')
#                 trav(n.left)
#                 # print('r_call')
#                 trav(n.right)
#                 p.pop()
#             return c[0]

#         return trav(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# doesnt make much sense...
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, max_val):
            nonlocal count
            if not node:
                return 
            elif node.val >= max_val:
                max_val = node.val
                count += 1

            dfs(node.left, max_val)
            dfs(node.right, max_val)
        
        dfs(root, root.val)
        return count
















