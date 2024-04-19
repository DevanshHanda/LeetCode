# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         visited = set()
#         def dfs(i,j):         
#             if grid[i][j]=='0':
#                 return    
#             if grid[i][j]=='1' and (i,j) not in visited:
#                 visited.add((i,j))
#                 # if 0<=i<len(grid) and 0<=j<len(grid[-1]) and (i,j) not in visited:
#             if (i+1,j) not in visited:
#                 try:
#                     dfs(i+1,j)
#                 except:
#                     pass
#             # print(1,i,j)
#             if (i,j+1) not in visited:
#                 try:
#                     dfs(i,j+1)
#                 except:
#                     pass
#             # print(1,i,j)
#             if (i-1,j) not in visited:
#                 try:
#                     dfs(i-1,j)
#                 except:
#                     pass
#             # print(1,i,j)
#             if (i,j-1) not in visited:
#                 try:
#                     dfs(i,j-1)
#                 except:
#                     pass
#             # print(1,i,j)

#         c=0
#         for i in range(len(grid)):
#             for j in range(len(grid[-1])):
#                 if grid[i][j]=='1' and (i,j) not in visited:
#                     dfs(i,j)
#                     c+=1
#         # print(visited)
#         return c
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '0'  # mark as visited
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands