
class Solution:
    def trap(self, height: List[int]) -> int:
        # finding the left max traversing from left to right.
        n = len(height)
        l = [0]*n
        lmax, rmax = 0, 0

        for i,v in enumerate(height):
            l[i]=lmax
            if v>lmax:
                lmax = v
        # print(l)
        # finding the right max traversing from right to left
        r = [0]*n
        for i,v in enumerate(height[::-1]):
            r[n-i-1]=rmax
            if v>rmax:
                rmax = v
        # print(r)
        # print(height)
        water = [0]*n
        for i in range(n):
            t = min(l[i],r[i])-height[i]
            if t>0:
                water[i] = t
        # print(water)
        # print()
        return sum(water)

            