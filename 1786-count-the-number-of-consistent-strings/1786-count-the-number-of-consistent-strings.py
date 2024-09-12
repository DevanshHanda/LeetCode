class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        def make(word):
            return set([i for i in word])
        c = 0
        k = make(allowed)
        for i in words:
            s = make(i)
            if not s-k:
                c+=1
        return c

