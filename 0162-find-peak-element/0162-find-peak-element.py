class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def bins(i,j):
            
            if i==j:
                return -1
            if i+1==j:
                mid = i+1
                if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                    return mid
                mid-=1
                if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                    return mid

                return -1
            mid = i+(j-i)//2
            print(i,j,mid)
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            c = bins(mid,j)
            d = bins(i,mid)
            if c!=-1:
                return c
            elif d!=-1:
                return d
            else: 
                return -1
        if len(nums)==1:
            return 0

        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1

        
        if len(nums)==3:
            mid = 1
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
        if len(nums)==4:
            mid = 1
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            mid = 2
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            
        return bins(1,len(nums)-2)

