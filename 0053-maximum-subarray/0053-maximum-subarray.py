class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # storing the max sum wrt each index in dict (used as a pointer)
        # leads to O(n^2) need a better solution.
        # d = dict()
        # for i,v in enumerate(nums):
        #     ma = v
        #     d[i] = v
        #     for j in nums[i+1:]:
        #         ma+=j
        #         if ma>d[i]:
        #             d[i]=ma
                    
        # return max(list(d.values()))



        # people are using Kadane's algorithm O(n)
        ms = [nums[0]]
        for i in nums[1:]:
            if ms[-1]>=0:
                ms.append(ms[-1]+i)
            else:
                ms.append(i)

        return max(ms)



