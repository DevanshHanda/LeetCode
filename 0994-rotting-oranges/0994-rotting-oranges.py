class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        loc2 = {(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2}
        loc1 = {(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1}
        d = [(-1,0),(0,-1),(1,0),(0,1)]
        newbie = set()
        c=0
        f=False
        # print(loc1)
        for (i,j) in loc2:
            for k in d:
                if (i+k[0],j+k[1]) in loc1:
                    f=True
                    loc1.remove((i+k[0],j+k[1]))
                    newbie.add((i+k[0],j+k[1]))
        if f:
            # print(loc1)
            c+=1
            f=False
        # print('naam',newbie)

        noob = set()
        while loc1:
            f=False
            for (i,j) in newbie:
                for k in d:
                    if (i+k[0],j+k[1]) in loc1:
                        
                        f=True
                        loc1.remove((i+k[0],j+k[1]))
                        noob.add((i+k[0],j+k[1]))
            if f:
                # print(loc1)
                c+=1
                f=False
            newbie = noob.copy()
            # print('naam',newbie)
            if not noob:
                return -1
            noob=set()
        return c
