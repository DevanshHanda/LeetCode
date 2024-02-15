class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        print(nums)
        s=sum(nums)
        for i in nums:
            if s-i<=i:
                s-=i
        if s==0:
            return -1
        return s

