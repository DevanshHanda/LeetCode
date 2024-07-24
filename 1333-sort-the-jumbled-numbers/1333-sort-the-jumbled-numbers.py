class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d={str(i):v for i,v in enumerate(mapping)}
        # print(d)
        d[' ']=0
        k = len(str(max(nums)))
        # print(k)
        nums = [ ' ' * (k-len(str(i))) + str(i) for i in nums ]
        # print(nums)
        for i in range(k-1,-1,-1):
            nums.sort(key=lambda x: d[x[i]])
            # print(nums)
        
        nums = [int(i) for i in nums]
        return nums
