class Solution:
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     # dp = [[0]*len(text1)]
    #     t=[]
    #     for i in text1:
    #         if i!=text2[0]:
    #             t.append(0)
    #         else:
    #             t.append(1)
    #     dp = [t]

    #     for i in range(1,len(text2)):
    #         if text2[i]==text1[0]:
    #             dp.append([1]+[0]*(len(text1)-1))
    #         else:
    #             dp.append([0]*len(text1))
    #         # dp.append(dp[0])


    #     print(dp)

    #     for i in range(1,len(text2)):
    #         for j in range(1,len(text1)):
    #             if text1[j]==text2[i]:
    #                 dp[i][j]=max(1,dp[i][j-1],dp[i-1][j],dp[i-1][j-1]+1)
    #             else:
    #                 dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        
    #     p=[]
    #     for i in dp:
    #         p+=[i]
    #     print(dp)
    #     return max(p)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                dp[i + 1][j + 1] = 1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]
            