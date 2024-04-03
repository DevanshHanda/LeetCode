# class Solution:
    
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         if len(board)==1:

#         def neigh(i,j):
#             # print(i,j)
#             # print(d)
#             if i==0 and j==0:
#                 return [(board[i+1][j],i+1,j),(board[i][j+1],i,j+1)]
#             elif i==len(board)-1 and j==0:
#                 return [(board[i][j+1],i,j+1),(board[i-1][j],i-1,j)]
#             elif i==0 and j==len(board[0])-1:
#                 return [(board[i][j-1],i,j-1),(board[i+1][j],i+1,j)]
#             elif i==len(board)-1 and j==len(board[0])-1:
#                 return [(board[i][j-1],i,j-1),(board[i-1][j],i-1,j)]
#             elif i==0 :
#                 return [(board[i+1][j],i+1,j),(board[i][j+1],i,j+1),(board[i][j-1],i,j-1)]
#             elif j==0:
#                 return [(board[i+1][j],i+1,j),(board[i][j+1],i,j+1),(board[i][j-1],i,j-1)]
#             elif j==len(board[0])-1:
#                 return [(board[i+1][j],i+1,j),(board[i][j-1],i,j-1),(board[i-1][j],i-1,j)]
#             elif i==len(board)-1:
#                 return [(board[i][j-1],i,j-1),(board[i][j+1],i,j+1),(board[i-1][j],i,j-1)]
#             else:
#                 return [(board[i+1][j],i+1,j),(board[i][j+1],i,j+1),(board[i][j-1],i,j-1),(board[i-1][j],i-1,j)]
        
#         d=dict()
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if (board[i][j],i,j) not in d:
#                     d[(board[i][j],i,j)] = neigh(i,j)
#         # print(d)
        
#         def walk(i,k,visited=[]):
#             visited.append(k)
#             if i==len(word)-1:
#                 return True
#             f = False
#             for (x,y,z) in d[k]:
#                 if x==word[i+1]:
#                     if (x,y,z) not in visited:
#                         # print(x,y,z)
#                         f = walk(i+1,(x,y,z))
#                 if f:
#                     return True
#             visited.pop()
#             return False
        
#         for a,b,c in d:
#             f=False
#             # print(a,b,c)
#             if a==word[0]:
#                 # print(a,b,c)
#                 f = walk(0,(a,b,c))
#             if f:
#                 return True
#         return False

#         # return walk(w[0],0,)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        R = len(board)
        C = len(board[0])
        
        if len(word) > R*C:
            return False
        
        count = Counter(sum(board, []))
        
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
            
        if count[word[0]] > count[word[-1]]:
             word = word[::-1]
                        
        seen = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= R or c >= C or word[i] != board[r][c] or (r,c) in seen:
                return False
            
            seen.add((r,c))
            res = (
                dfs(r+1,c,i+1) or 
                dfs(r-1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1) 
            )
            seen.remove((r,c))  #backtracking

            return res
        
        for i in range(R):
            for j in range(C):
                if dfs(i,j,0):
                    return True
        return False




                