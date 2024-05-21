class Solution:
    def tribonacci(self, n: int,p=[0],q=[0]) -> int:
        p = [0,1,1]
        p=p+[0]*(n-2)
        for i in range(3,n+1):
            p[i] = p[i-2]+p[i-3]+p[i-1]
        return p[n]
            

