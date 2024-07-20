class StockSpanner:

    def __init__(self):
        self.ans=[]
        # self.sa=1
        

    def next(self, price: int) -> int:
        cur = self.ans

        s = 1
        if len(cur)==0:
            cur.append([price,s])
            return s

        while cur and cur[-1][0]<=price:
            thro,t = cur.pop()
            s+=t
        cur.append([price,s])
        return s


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)