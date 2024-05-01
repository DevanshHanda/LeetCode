class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            t = word.index(ch)
            s = word[0:t+1]
            return s[::-1]+word[t+1:]
        except:
            return word
            