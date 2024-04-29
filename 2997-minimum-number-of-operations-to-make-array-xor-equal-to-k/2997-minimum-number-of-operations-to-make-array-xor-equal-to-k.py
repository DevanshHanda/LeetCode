class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # nums = [6,1,2,4]
        # nums = ["{0:b}".format(nc) for nc in nums]
        s=nums[0]
        for i in range(1,len(nums)):
            s=s^nums[i]
        print(s)

        t1 = "{0:b}".format(s)
        t2 = "{0:b}".format(k)
        if len(t1)>len(t2):
            t2 = '0'*(len(t1)-len(t2))+t2
        elif len(t2)>len(t1):
            t1 = '0'*(len(t2)-len(t1))+t1
        
        
        c=0
        for i in range(len(t1)):
            if t1[i]!=t2[i]:
                c+=1
        return c