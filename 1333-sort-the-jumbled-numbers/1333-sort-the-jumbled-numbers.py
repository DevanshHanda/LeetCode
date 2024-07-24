class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d={str(i):v for i,v in enumerate(mapping)}
        d[' ']=0
        k = len(str(max(nums)))
        nums = [ ' ' * (k-len(str(i))) + str(i) for i in nums ]
        
        # Radix sort
        for i in range(k-1,-1,-1):
            nums.sort(key=lambda x: d[x[i]])
           
        nums = [int(i) for i in nums]
        return nums
