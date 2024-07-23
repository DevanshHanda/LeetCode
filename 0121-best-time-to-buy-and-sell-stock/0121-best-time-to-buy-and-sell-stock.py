class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # holdi0,holdi1 = 0,-float('inf')
        # for i in prices:
        #     previ0 = holdi0
        # print money my honey bunny(crrazy)


        # # Kadane's Algorithm
        # max_so_far = float('-inf')  
        # # Use float('-inf') instead of maxint
        # max_ending_here = 0
        # for i in range(0, size):
        #     max_ending_here = max_ending_here + a[i]
        #     if max_so_far < max_ending_here:
        #         max_so_far = max_ending_here
        #     if max_ending_here < 0:
        #         max_ending_here = 0
        # return max_so_far

        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
            
        return max_profit 
