class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        h0 = 0
        h1 = -float('inf')

        for price in prices:
            prev0 = h0
            h0 = max(prev0,h1+price)
            h1 = max(h1,h0-price)
        return h0
