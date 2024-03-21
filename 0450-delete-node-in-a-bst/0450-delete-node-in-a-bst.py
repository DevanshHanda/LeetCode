# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# First find the node that we need to delete.
# After it's found, think about ways to keep the tree BST after deleting the node.
# If there's no left or right subtree, we found the leaf. Delete this node without any further traversing.
# If it's not a leaf node, what node we can use from the subtree that can replace the delete node and still maintain the BST property? We can either replace the delete node with the minimum from the right subtree (if right exists) or we can replace the delete node with the maximum from the left subtree (if left exists).



class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
	    if not root:
		    return None

	    if key > root.val:
		    root.right = self.deleteNode(root.right, key)
	    elif key < root.val:
		    root.left = self.deleteNode(root.left, key)
	    else:
		    if not root.left and not root.right:
			    root = None
		    elif root.right:
			    root.val = self.successor(root)
			    root.right = self.deleteNode(root.right, root.val)
		    else:
			    root.val = self.predecessor(root)
			    root.left = self.deleteNode(root.left, root.val)
	    return root

    def successor(self, root: TreeNode) -> TreeNode:
	    root = root.right
	    while root.left:
		    root = root.left
	    return root.val

    def predecessor(self, root: TreeNode) -> TreeNode:
	    root = root.left
	    while root.right:
		    root = root.right
	    return root.val
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         if not root:
#             return root
#         t = root
#         prev = root
#         # finding the key, if not found return the root as is.
#         while t.val!=key:
#             prev = t
#             print(prev.val,t.val)
#             if t.val>key:
#                 if not t.left:
#                     return root
#                     break
#                 t=t.left
#             elif t.val<key:
#                 if not t.right:
#                     return root
#                     break
#                 t=t.right
        
#         print(t.val)
#         print(prev.val)
#         # check if leaf node, then delete
#         # if not t.left and not t.right:
#         # return None

#         if not t.left and not t.right:
#             if prev.val > t.val:
#                 prev.left = None
#             elif prev.val < t.val:
#                 prev.right = None
#             if prev.val == t.val:
#                 return None
#             return root

#         # check if has right subtree
#         if t.right :
#             # return minimum in right subtree
#             p = t.right
#             try:
#                 while p.left.left:
#                     p=p.left
#                 t.val = p.left.val
#                 print(t.val)
#                 p.left = None
#                 return root
#             except:
#                 t.val = p.val
#                 t.right = p.right
#                 return root
#         if t.left:
#             # return max in left sub tree
#             p = t.left
#             try:
#                 while p.right.right:
#                     p=p.right
#                 t.val = p.right.val
#                 print(t.val)
#                 p.right = None
#                 return root
#             except:
#                 t.val = p.val
#                 t.left = p.left
#                 return root
            


            
            


