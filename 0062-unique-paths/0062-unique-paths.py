class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]+[1]*(n-1)]
        for k in range(m-1):
            dp.append([1]+[0]*(n-1))
        # for i in dp:
        #     print(i)
        for i in range(1,m):
            for j in range(1,n):
                # print(i,j)
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]