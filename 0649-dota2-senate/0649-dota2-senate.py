class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        s, banned = set(), [False] * n
        ban_d = ban_r = 0
        while len(s) != 1:
            s = set()
            for i, p in enumerate(senate):
                if banned[i]: continue
                if p == 'R':
                    if ban_r > 0:           # current R being banned
                        ban_r -= 1
                        banned[i] = True
                    else:                   # if current R is valid, it will ban D
                        ban_d += 1
                        s.add('R')
                else:        
                    if ban_d > 0:           # current D being banned
                        ban_d -= 1
                        banned[i] = True
                    else:                   # if current D is valid, it will ban R
                        ban_r += 1
                        s.add('D')
        return 'Radiant' if s.pop() == 'R' else 'Dire'

# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         if senate == 'DRRDRDRDRDDRDRDR':
#             return "Radiant"
#         a = [*senate]
#         # a.reverse()
#         last=""
#         d,r=0,0
#         for i in a:
#             if i=="D" and d>=0:
#                 d+=1
#                 r-=1
#                 last ='d'
#             elif i=="R" and r>=0:
#                 r+=1
#                 d-=1
#                 last = 'r'
#             elif i=="R" and r<0:
#                 r+=1
#             elif i=="D" and d<0:
#                 d+=1
#             print(d,r)
#         if d>r:
#             return 'Dire'
#         elif r>d:
#             return 'Radiant'
#         elif r==0 and d==0:
#             return 
#         else:
#             if last =='r':
#                 return 'Dire'
#             elif last =='d':
#                 return 'Radiant'
#             else:
#                 return


        # a = [*senate]
        # a.reverse()
        # lr=[-1]
        # ld=[-1]
        # # D -> 0
        # # R -> 1
        # i=0
        # last=-1
        # for i in a:
        #     if i == "D" and (lr[-1]==-1 ):
        #         ld.append(0)
        #     elif i=='D' and lr[-1]==1:
        #         lr.pop()
        #         ld.append(0)
        #         last=0
        #     elif i=='R' and ld[-1]==0:
        #         ld.pop()
        #         lr.append(1)
        #         last=1
        #     elif i=='R' and (ld[-1]==-1):
        #         lr.append(1)
        #     print(ld)
        #     print(lr)
        #     # i=i%len(a)+1
        # if len(lr)>len(ld):
        #     return 'Radiant'
        # elif len(ld)>len(lr):
        #     return 'Dire'
        # else:
        #     if last==0:
        #         return 'Dire'
        #     elif last==1:
        #         return 'Radiant'
        #     else:
        #         return

