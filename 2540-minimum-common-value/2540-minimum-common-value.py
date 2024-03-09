class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # l = [s for s in nums1 if s in nums2]
        # if l:
        #     return min(l)
        # else:
        #     return -1
        if nums1[-1]<nums2[0]:
            return -1
        s1 = set(nums1)
        s2 = set(nums2)
        sp = s1 & s2
        # print(sp)
        if sp:
            return min(sp)
        else :
            return -1