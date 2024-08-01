class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0)>1:
            return [0]*len(nums)
        
        t=1
        for i in nums:
            if i!=0:
                t*=i

        if 0 in nums:
            ind = nums.index(0)
            return [0]*ind+[int(t)]+[0]*(len(nums)-ind-1)
        else:
            return [int(t/i) for i in nums]
        