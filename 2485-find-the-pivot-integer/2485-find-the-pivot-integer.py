class Solution:
    def pivotInteger(self, n: int) -> int:
        t = n*(n+1)/2
        # s = 0
        # for i in range(1,n+1):
        #     s+=i
        #     if s == -s+t+i:
        #         return i
            
        # return -1
        k = n*(n+1)/2
        for i in range(1,n+1):
            t = i*(i+1)/2
            if t==k-t+i:
                return i
        return -1

