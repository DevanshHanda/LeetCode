class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

# paying fee while buying
# i will have bigger chalanges in life and god will give me strength
        hold_i0,hold_i1 = 0,float('-inf')
        for i in prices:
            prev_hold_i0 = hold_i0

            hold_i0 = max(hold_i0,hold_i1+i)
            hold_i1 = max(hold_i1,prev_hold_i0-i-fee)
        return hold_i0

# public int maxProfit(int[] prices, int fee) {
#     int T_ik0 = 0, T_ik1 = Integer.MIN_VALUE;
    
#     for (int price : prices) {
#         int T_ik0_old = T_ik0;
#         T_ik0 = Math.max(T_ik0, T_ik1 + price);
#         T_ik1 = Math.max(T_ik1, T_ik0_old - price - fee);
#     }
        
#     return T_ik0;
# }