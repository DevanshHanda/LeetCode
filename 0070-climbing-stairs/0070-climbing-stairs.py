class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        def cow(y,l):
            # nClen(l)
            # print('out of',l,'choosing',y,l-y)
            return fact(l)/(fact(y)*fact(l-y))

        def fact(y):
            if y==0 or y==1:
                return 1
            p=1
            while y>1:
                p*=y
                y-=1
            return p
        
        if n%2==0:
            zer=0
        else:
            zer=1
        k = int(n/2)
        t = n
        d=1
        for i in range(1,k+1):
            t -=1
            d += cow(i,t)

        return int(d)