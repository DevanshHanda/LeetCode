class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def fn(cond): 
            """Return topological sort"""
            graph = [[] for _ in range(k)]
            indeg = [0]*k
            for u, v in cond: 
                graph[u-1].append(v-1)
                indeg[v-1] += 1
            queue = deque(u for u, x in enumerate(indeg) if x == 0)
            ans = []
            while queue: 
                u = queue.popleft()
                ans.append(u+1)
                for v in graph[u]: 
                    indeg[v] -= 1
                    if indeg[v] == 0: queue.append(v)
            return ans 
        
        row = fn(rowConditions)
        col = fn(colConditions)
        
        if len(row) < k or len(col) < k: return []
        ans = [[0]*k for _ in range(k)]
        row = {x : i for i, x in enumerate(row)}
        col = {x : j for j, x in enumerate(col)}
        for x in range(1, k+1): ans[row[x]][col[x]] = x
        return ans 

        
# Dedicated and results-oriented Software Development Engineer in Test (SDET) 
# with a proven track record in automation (UI/API), API testing, Benchmarking, 
# and Behavior-Driven Development (BDD). Proficient in a wide range of tools and 
# technologies, including Selenium WebDriver, pytest, behave, Request Library, JMeter
# , and Python scripting. Expertise spans black-box Testing, Regression Testing, ensuring
# meticulous attention to detail in meeting functional and non-functional requirements. 
# Thrives in dynamic environments, utilizing automation to optimize efficiency and 
# quality across the software development lifecycle.