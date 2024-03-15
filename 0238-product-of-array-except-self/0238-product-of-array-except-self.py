class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0)>1:
            return len(nums)*[0]
        c=1
        if nums.count(0)==1:
            for i in nums:
                if i!=0:
                    c*=i
            d = nums.index(0)
            x = len(nums)*[0]
            x[d] = c
            return x

        for i in nums:
            if i!=0:
                c*=i
        
        x = [int(c/i) for i in nums]
        return x