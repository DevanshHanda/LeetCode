class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 += nums2
        nums1.sort()
        while 0 in nums1 and len(nums1)>n+m:
            nums1.remove(0)
            # if 0 in 
        
        