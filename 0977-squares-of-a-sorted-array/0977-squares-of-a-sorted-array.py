class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        k = [x**2 for x in nums]
        return sorted(k)