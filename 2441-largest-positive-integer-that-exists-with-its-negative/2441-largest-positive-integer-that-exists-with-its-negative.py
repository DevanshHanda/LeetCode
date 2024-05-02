class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        n = {-i for i in nums if i<0}
        p = {i for i in nums if i>0}
        try:
            return max(n.intersection(p))
        except:
            return -1


