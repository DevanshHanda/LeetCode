class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        s = sorted(happiness)
        tot = 0
        for i in range(k):
            t = s.pop()
            tot += t
            try:
                s[-1]-=(i+1)
                if s[-1]<=0:
                    break
            except:
                break
        return tot
