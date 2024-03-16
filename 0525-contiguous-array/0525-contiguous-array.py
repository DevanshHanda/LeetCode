class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        sum_val = 0
        max_len = 0
        for i, num in enumerate(nums):
            sum_val += 1 if num == 1 else -1
            if sum_val == 0:
                max_len = i + 1
            elif sum_val in mp:
                max_len = max(max_len, i - mp[sum_val])
            else:
                mp[sum_val] = i
        return max_len
        # begining with 0
        # m=0
        # for i in range(len(nums)):
        #     for j in range(i+2,len(nums)+1):
        #         # print(nums[i:j])
        #         if nums[i:j].count(1)==nums[i:j].count(0):
        #             if j-i>m :
        #                 m=j-i
        # # return m
        # a = nums.count(0)
        # b = nums.count(1)
        # print(len(nums))
        # print('0:',a)
        # print('1:',b)
        # if a>b:
        #     t=[]
        #     for i in range(len(nums)):
        #         if nums[i]==0:
        #             t.append(i)
        #     for i in range(len(t)):
        #         if t[i]-t[0]>2*b:
        #             return 2*i
        #     return 2*b
        # elif b>a:
        #     t=[]
        #     for i in range(len(nums)):
        #         if nums[i]==0:
        #             t.append(i)
        #     print(t)
        #     for i in range(len(t)):
        #         if t[i]-t[0]>2*a:
        #             return 2*i
        #     return 2*a
        # return 2*a

        # # return 2*min(a,b)

        # # z,o,m=0,0,0
        # # for i in nums:
        # #     if i==0:
        # #         z+=1
        # #     if i==1:
        # #         o+=1
        # #     if o==z:
        # #         if m<o+z:
        # #             m = o+z
        # # return m

            