# class Solution:
#     def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        # a = sorted(maximumHeight)[::-1]
        # # l = [0]*(a[0]+1)/
        # l = set()
        # sum=0
        # print(l)
        # r = 0
        # for i in a:
        #     # print(l)
        #     if i not in l:
        #         l.add(i)
        #     else:
        #         k=i
        #         # print(k)
        #         while k in l and k>=1:    
        #             k-=1
        #         # print(k)
        #         if k==0:
        #             return -1
        #         l.add(k)
        # # print(l,r)
        # return sum(l)
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        a = sorted(maximumHeight)[::-1]
        n = a[0]
        s=0
        for i,v in enumerate(a):
            n = min(n,v)
            if n<=0:
                return -1
            s+=n
            n-=1
        return s