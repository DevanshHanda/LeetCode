import collections
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        de = []
        def shift(l):
            try:
                return [l.pop()] + l
            except:
                return l
        for i in deck:
            de=[i]+shift(de)
        return de
