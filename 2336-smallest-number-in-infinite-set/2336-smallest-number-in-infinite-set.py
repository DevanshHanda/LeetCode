class SmallestInfiniteSet:

    def __init__(self):
        self.s = [1]

    def popSmallest(self) -> int:
        if len(self.s)==1:
            self.s[0]+=1
            return self.s[0]-1
        else:
            t = self.s[0]
            self.s.remove(t)
            return t
        

    def addBack(self, num: int) -> None:
        if num<max(self.s) and num not in self.s:
            self.s=[num]+self.s
            self.s.sort()
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)