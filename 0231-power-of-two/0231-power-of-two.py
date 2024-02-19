class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        # print(int(log(n, 2)),log(n,2))
        return int(log(n, 2))-log(n,2)>-0.000000000001
        
        # if n==0:
        #     return False
        
        # while True:
        #     if n==1:
        #         return True
        #     r = n%2
        #     n = int(n/2)
        #     if r==1:
        #         return False

        