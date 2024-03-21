# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # k = len(rooms)
        # k = set([i for i in range(k)])
        # d = {i:False for i in k}
        # i = 0
        # keys = [0]
        # while True:
        #     t = rooms[i]
        #     keys += list(set(t))
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        if not rooms or not rooms[0]:
            return False
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in rooms[node]:
                if nei == node:
                    continue
                dfs(nei)
        
        dfs(0)
        if len(visited) == len(rooms):
            return True
        return False
        

        # d = {i:[False,rooms[i]] for i in range(len(rooms))}
        # d[0][0]=True
        # for k in range(int(len(rooms))):
        #     for i in d:
        #         if d[i][0]:
        #             for j in d[i][1]:
        #                 if not d[j][0]:
        #                     print(j)
        #                     d[j][0]=True
        # t = True
        # for i in d:
        #     print(d[i][0])
        #     t = t and d[i][0]
        #     if not t:
        #         return t
        # return t


