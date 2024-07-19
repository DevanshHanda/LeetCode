class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # min in row, max in col
        l=[]
        for _ in range(len(matrix[0])):
            l.append([]) 
        
        for i,k in enumerate(matrix):
            for j,p in enumerate(k):
                # if j==i:
                    l[j].append(p)
        
        max_c = []
        min_r = []
        for i in l:
            max_c.append(max(i))
        for j in matrix:
            min_r.append(min(j))
        
        # print(set(max_c)-(set(max_c) - set(min_r)))
        return list(set(max_c)-(set(max_c) - set(min_r)))

        # print(l)


        
