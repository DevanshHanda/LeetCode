class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d={}
        for i,a in enumerate(equations):
            if a[0] not in d:
                d[a[0]]=dict()
            if a[-1] not in d:
                d[a[-1]]=dict()
            # print(a,i)
            d[a[0]][a[-1]]=values[i]
            d[a[-1]][a[0]]=1/values[i]
        # print(d)
        # c=1
        l=[]

        def dfs(c,t,visited):
            # print(c,t)
            if c in visited:
                return -1
            if c not in d:
                return -1
            if t in d[c]:
                visited.add(c)
                return d[c][t]

            elif t not in d[c]:
                visited.add(c)
                for i in d[c].keys():
                    if i not in visited:
                        p= dfs(i,t,visited)
                        if p==-1: 
                            continue
                        else: return d[c][i] * p
            return -1 
            
        
        for i,b in enumerate(queries):
            visited=set()
            if b[0] not in d or b[-1] not in d:
                l.append(-1)
            else:
                l.append(dfs(b[0],b[-1],visited))
        return l

