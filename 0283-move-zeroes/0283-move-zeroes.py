class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # j=0
        # i=0
        # while i<len(nums)-nums.count(0):
        #     if nums[i]==0:
        #         for j in range(i,len(nums)-1):
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        #         i-=1
        #     i+=1
        a = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[a],nums[i]=nums[i],nums[a]
                a+=1
        
        
        