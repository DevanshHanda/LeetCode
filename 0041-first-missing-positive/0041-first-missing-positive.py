class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l=[i for i in range(1,len(nums)+1)]
        l=set(l)
        k=set(nums)
        j = l-k
        if j:
            return min(j)
        else:
            return max(nums)+1
