class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        l=[]
        diff = []
        for i,v in enumerate(gas):
            tank+=v-cost[i]
            diff.append(v-cost[i])
            l.append(tank)
        # print(l)
        t = min(l)
        # print(t)
        l = [i-t for i in l]
        # print(min(l))
        l_temp=[]
        l_temp[:] = l[::-1]
        ind = (len(l)-l_temp.index(0))%len(gas)
        parse = l[ind:]+l[:ind]
        diff = diff[ind:]+diff[:ind]
        tank=0
        j=0
        for i in parse:
            # print(tank,i,diff[j])
            tank+=diff[j]
            j+=1
            if i > tank:
                return -1

        return ind
