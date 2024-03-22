class Solution:
    def countBits(self, n: int) -> List[int]:
        return [k.count('1') for k in ['{0:b}'.format(i) for i in range(n+1)]]
        