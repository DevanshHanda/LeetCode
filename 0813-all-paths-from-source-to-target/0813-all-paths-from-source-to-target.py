class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        po=[0]
        res=[]

        def dfs(node):
            if node==(n-1):
                res.append(po.copy())

            for i in graph[node]:
                po.append(i)
                dfs(i)
                po.pop()
        
        dfs(0)
        return res
                

                    
                