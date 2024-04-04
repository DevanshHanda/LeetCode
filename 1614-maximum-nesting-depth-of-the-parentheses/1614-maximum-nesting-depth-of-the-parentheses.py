class Solution:
    def maxDepth(self, s: str) -> int:
        k=0
        m=0
        for i in s:
            if i == '(':
                k+=1
            elif i==')':
                k-=1
            if m<k:
                m=k
        return m

            