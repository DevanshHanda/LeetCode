class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # i=0
        # time limit exceeded for inplace
        n=len(nums)
        k=k%n
        # for _ in range(k):
        #     a = nums[(k+1)%n]
        #     nums[(k+1)%n]=nums[(k)%n]

        #     t = (k+2)%n

        #     while t!=(k+1)%n:
        #         a,nums[t] = nums[t],a
        #         t=(t+1)%n

        nums[:]=  nums[n-k:]+nums[:n-k]