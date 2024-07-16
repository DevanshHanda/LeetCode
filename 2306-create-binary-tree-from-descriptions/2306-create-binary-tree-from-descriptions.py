# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # print(900000000)

        # d=[descriptions[0][0]]
        # root = TreeNode(descriptions[0][0])
        # print(root)

        # child = descriptions[0][1]
        # if descriptions[0][2]==0:
        #     root.right = TreeNode(child)
        #     d.append(child)
        # elif descriptions[0][2]==1:
        #     root.left = TreeNode(child)
        #     d.append(child)
        
        # descriptions.remove(descriptions[0])

        # def findNode(v,t):
        #     # print(t.val)
        #     if t:
        #         print(t.val)
        #         if t.val==v:
        #             return t
        #         else:
        #             t1 = findNode(v,t.left)
        #             if t1:
        #                 return t1
        #             t2 = findNode(v,t.right)
        #             if t2:
        #                 return t2

        # # def findNode(v, t):
        # #     if t is None:  # If current node is None, return None
        # #         return None
        # #     print(t.val)  # Optional: Print the current node's value for debugging
        # #     if t.val == v:
        # #         return t  # Node found, return it
        # #     # Recurse in left subtree
        # #     t1 = findNode(v, t.left)
        # #     if t1:
        # #         return t1  # Node found in the left subtree, return it
        # #     # Recurse in right subtree only if not found in left
        # #     return findNode(v, t.right)

        # def findrep(n):
        #     for i in d:
        #         if n in i:
        #             return i
        #     return None

        # def addprep(n):
        #     for i in d:
        #         if n in i:
        #             i.append(n)

        # # for parent, child, k in descriptions:
        # #     # print(root)
        # #     print(parent, child, k)

        # #     parent_tree = findrep(parent)
        # #     if parent_tree:
        # #         print('parent not there')
        # #         temp = TreeNode(parent)
        # #         addprep(parent)

        # #         child_tree = findrep(parent)
        # #         if child_tree:
        # #             print('child there')
        # #             found = findNode(child,root)# which root im giving it to
        # #             if k==0:
        # #                 temp.right = found
        # #                 addprep(parent)
        # #             elif k==1:
        # #                 temp.left = found
        # #                 addprep(child)
        # #             root = temp
        # #         else:
        # #             print('child not there')
                    
                
        # #     else:
        # #         print('parent there')
        # #         temp = findNode(parent,root)

        # #         if child not in d:  
        # #             print('child not there')
        # #             if k==0:
        # #                 temp.right = TreeNode(child)
        # #                 d.append(child)
        # #             elif k==1:
        # #                 temp.left = TreeNode(child)
        # #                 d.append(child)

        # for parent, child, k in descriptions:
             

            
            
        # 1 = left
        # 0 = right
        # return root
        d = {}
        p=[]
        c=[]
        for parent, child, k in descriptions:
            p.append(parent)
            c.append(child)
            if parent not in d:
                d[parent]=[None,None]
            d[parent][k]=child

        rc = (set(p)-set(c)).pop()
        root = TreeNode(rc)
        print(root)
        print(d)
        
        def build(r):
            if r.val in p:
                # print(r.val)
                if d[r.val][0]:
                    r.right = TreeNode(d[r.val][0])
                    build(r.right)
                if d[r.val][1]:
                    r.left = TreeNode(d[r.val][1])
                    build(r.left)

        build(root)
        return root

            


        
        
                




        
        
# [[85,82,1],[74,85,1],[39,70,0],[82,38,1],[74,39,0],[39,13,1]]

