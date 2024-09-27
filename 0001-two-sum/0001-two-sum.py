class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using conecpt of hashmaps ( dict ) where the key is just looked up and not searched.
        d = dict()
        for i,v in enumerate(nums):
            
            if target - v in d:
                return [i,d[ target - v ]]
            d[v] = i
            
        