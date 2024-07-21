class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # m = candies.index(max(candies))
        t = max(candies)
        return [i+extraCandies>=t for i in candies]
        # return [True]*(m+1)+[False]*(len(candies)-m-1)
