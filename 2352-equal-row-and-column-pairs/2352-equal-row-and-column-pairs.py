class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c=[]
        for i in range(len(grid)):
            c.append([])
            for j in range(len(grid)):
                c[i].append(grid[j][i])
      
        for i in range(len(c)):
            for j in range(len(c)):
                c[i][j]='.'+str(c[i][j])
                grid[i][j]='.'+str(grid[i][j])
            c[i]=''.join(c[i])
            grid[i]=''.join(grid[i])
       
        f1 = {char:c.count(char) for char in c}
        f2 = {char:grid.count(char) for char in grid}

        print(f1,f2)
        common = set(f1.keys())-(set(f1.keys())-set(f2.keys()))
        count=0
        for i in common:
            count+=f1[i]*f2[i]
        return count

        # pairs = 0
        # cnt = Counter(tuple(row) for row in grid)
        # for tpl in zip(*grid):
        #     pairs += cnt[tpl]
        # return pairs