class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # k=[]
        # i,j=0,0
        # n=len(nums)-1
        # while j<=n and i<=n:
        #     while(nums[i]<0):
        #         i+=1
        #     k.append(nums[i])
        #     i+=1
        #     while(nums[j]>=0):
        #         j+=1
        #     k.append(nums[j])
        #     j+=1
        # return k
        
        pos, neg = [], []
        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
        nums[0 : len(pos) * 2 : 2] = pos
        nums[1 : len(neg) * 2 : 2] = neg
        return nums


