class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # vertices with no in degree
        return list(set([i for i in range(n)]) - set([j for i,j in edges]))

        # d=dict()
        # ans=[]
        # ma=[]
        # per = [i for i in range(n)]
        # for i,j in edges:
        #     if i not in d:
        #         d[i]=[j]
        #     else:
        #         d[i].append(j)
        #     if len(d[i])==n:
        #         return [i] 
            
        #     if len(ma)<len(d[i]):
        #         ma = d[i]
        # t = list(set(per)-set(ma))

        