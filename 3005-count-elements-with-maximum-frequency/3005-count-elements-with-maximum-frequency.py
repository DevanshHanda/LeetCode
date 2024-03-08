class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d=dict()
        m=0
        c=0
        for i in set(nums):
            d[i] = nums.count(i)
            if d[i]>m:
                m = d[i]
                c = 0
            if d[i]==m:
                c+=1
        return c*m
        