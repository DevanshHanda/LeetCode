class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = tickets[k]
        gb = 0
        for i in range(k): 
            if tickets[i]>=t: 
                gb+=1
        # print(gb)
        tickets.sort()
        # print(tickets)
        s=0
        m = len(tickets)
        for x,i in enumerate(tickets):
            # print(x,i)
            s+=i
            # m-=1
            if i==t:
                # print(m,x)
                # print(f"{s}+{t}*{gb}+({t}-1)*({m}-{x}-1-{gb})")
                return s+t*gb+(t-1)*(m-x-1-gb)
        return 0
