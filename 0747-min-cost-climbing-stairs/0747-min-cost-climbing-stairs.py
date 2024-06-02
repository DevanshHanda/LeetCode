# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         def costf(cur,ind):
#             cur+=cost[ind]
#             if ind==0 or ind==1:
#                 return cur
#             else:
#                 if cost[ind-2]>cost[ind-1]:
#                     ind_new=ind-1
#                     # cur+=cost[ind_new]
#                     return costf(cur,ind_new)
#                 elif cost[ind-2]<cost[ind-1]:
#                     ind_new=ind-2
#                     # cur+=cost[ind_new]
#                     return costf(cur,ind_new)
#                 else:
#                     # cur+=cost[ind_new]
#                     return min(costf(cur,ind-1),costf(cur,ind-2))
                
#         # print(costf(0,len(cost)),costf(0,len(cost)-1))
#         # print(costf(0,len(cost)),cost[-2]+costf(0,len(cost)-1))
#         return min(costf(0,len(cost)-1),costf(0,len(cost)-2))
#         # return 0
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            # print(i)
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])



        
        
        