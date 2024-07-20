class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [k for k in set(nums) if nums.count(k)==1][0]