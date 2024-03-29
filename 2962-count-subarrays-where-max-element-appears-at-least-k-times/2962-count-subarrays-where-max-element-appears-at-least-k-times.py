class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ma = max(nums)
        p = nums.count(ma)
        if p<k:
            return 0
        t = nums.copy()
        li=[]
        for i in range(len(nums)):
            if nums[i]==ma:
                li.append(i)
        # s = set()
        # print(li)
        c=0
        for i in range(len(li)-k+1):
            if i==0:
                c+=(li[i]+1)*(len(nums)-li[i+k-1])
            else:
                c+= (li[i]-li[i-1])*(len(nums)-li[i+k-1])

        return c
        
            

        