class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, des in connections:
            adj[src].append((des,1))
            adj[des].append((src,0))

        visited = set()
        def dfs(src, count):
            visited.add(src)
            for des, change in adj[src]:
                if des not in visited:
                    count = dfs(des, count+change)
            return count
        return dfs(0,0)