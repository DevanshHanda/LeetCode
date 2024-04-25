class Solution:
        def longestIdealString(self, s, k):
            dp = [0] * 128
            for c in s:
                i = ord(c)
                dp[i] = max(dp[i - k : i + k + 1]) + 1
            return max(dp)
    # def longestIdealString(self, s: str, k: int) -> int:
    #     d = {i+str(x):[] for x,i in enumerate(s)}
    #     for x,i in enumerate(s):
    #         for j in range(x+1,len(s)):
    #             if abs(ord(i)-ord(s[j]))<=k:
    #                 d[i+str(x)].append(s[j]+str(j))
    #     p=[]
    #     def finds(i,f,k=[0]):
    #         if f:
    #             k[0]=0
    #             f=False
    #         # print(i,k,p)
    #         k[0]+=1
    #         if not d[i]:
    #             p.append(k[0])
    #             k[0]-=1
    #             return k[0]
    #         # m=0
    #         for j in range(len(d[i])):
    #             k[0] = max(finds(d[i][j],False),k[0])
    #         k[0]-=1
    #         return k[0]
    #     # print(d)
        
    #     for x,i in enumerate(d):
    #         finds(i,True)
    #         if max(p)>len(s)-x:
    #             break
    #         # print('once')
    #     # for i in d:
    #     # print(p)
    #     return max(p)


