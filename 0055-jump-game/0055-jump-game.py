# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         i=0
#         # print(nums)
#         range = nums[0]
#         # l = len(nums)
#         # print(l)
        
#         if len(nums)<2:
#             return True 
        
#         if nums[0]==0:
#             return False

#         while i+range<len(nums)-1:

#             print(nums[i],nums[i+1:i+range+1][::-1])
#             try:
#                 new_ma = max(nums[i+1:i+range+1])
#                 print(nums[i],nums[i+1:i+range+1][::-1].index(new_ma))
#                 new_ma_ind = nums[i+1:i+range+1][::-1].index(new_ma)-len(nums[i+1:i+range+1])+2
#             except:
#                 new_ma = nums[i+1]
#                 new_ma_ind = i+1
            
#             if new_ma==0:
#                 return False

#             i = new_ma_ind
#             range =  nums[i]

            

#         return True

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True