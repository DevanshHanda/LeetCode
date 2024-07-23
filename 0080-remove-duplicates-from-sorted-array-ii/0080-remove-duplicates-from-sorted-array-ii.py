class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # s = set(nums)
        d={}
        i=0

        while i<len(nums):
            # print(nums[:i+1])
            # print(d)
            if nums[i] in d:
                d[nums[i]]+=1
                if d[nums[i]]==3:
                    d[nums[i]]-=1
                    nums.remove(nums[i])
                    i-=1
                    
            else:
                d[nums[i]]=1
            # print(d)

            i+=1
        

