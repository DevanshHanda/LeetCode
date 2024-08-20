# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         tank = 0
#         l=[]
#         diff = []
#         for i,v in enumerate(gas):
#             tank+=v-cost[i]
#             diff.append(v-cost[i])
#             l.append(tank)
#         # print(l)
#         t = min(l)
#         # print(t)
#         l = [i-t for i in l]
#         # print(min(l))
#         l_temp=[]
#         l_temp[:] = l[::-1]
#         ind = (len(l)-l_temp.index(0))%len(gas)
#         parse = l[ind:]+l[:ind]
#         diff = diff[ind:]+diff[:ind]
#         tank=0
#         j=0
#         for i in parse:
#             # print(tank,i,diff[j])
#             tank+=diff[j]
#             j+=1
#             if i > tank:
#                 return -1

#         return ind
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #gas =  [2,3,4]
        #cost = [3,4,3]
        #total =-1,-1,1
        #sum of gas>= sum cost array
        sum_cost = sum(cost)
        sum_gas = sum(gas)
        # Check if it is possible to complete the journey
        if sum_cost > sum_gas:
            return -1

        current_gas = 0
        starting_index = 0

        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                starting_index = i + 1
        return starting_index
        