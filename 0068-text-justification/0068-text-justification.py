class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        def make_l(l):
            starting = ' '.join(l)
            ending = ' '*(maxWidth - len(starting))
            sentence = starting+ending
            return sentence

        def make(l):
            full = len(''.join(l))
            spaces = len(l)-1
            if spaces == 0:
                return make_l(l)
            avg = (maxWidth-full)//spaces
            extra = (maxWidth-full)%spaces
            list_spaces = []
            more_avg_space = ' '*(avg+1)
            avg_space = ' '*(avg)
            begining = more_avg_space.join(l[:extra+1])
            ending = avg_space.join(l[extra+1:])
            sentence = begining + avg_space + ending
            return sentence

        wordslen,cur=0,0
        ans = []
        for i,v in enumerate(words):
            wordslen+=len(v)+1
            if wordslen-1>maxWidth: # the len is not a simple calc
                wordslen=len(v)+1
                ans.append(make(words[cur:i]))
                cur = i
            if i==len(words)-1:
                ans.append(make_l(words[cur:]))

        return ans




























#         tc = 0
#         li = 0
#         # ans = ''
#         t = []
#         for i,v in enumerate(words):
#             tc+=len(v)+1
#             print(tc)
#             if tc>=maxWidth:
#                 tc-=1+len(v)
#                 gaps = i - li - 1
                
#                 if gaps == 0:
#                     # ans+= words[i-1]+' '*(maxWidth-tc-gaps)
#                     t.append(words[i-1]+' '*(maxWidth-tc-gaps))
#                     print(t)
#                 else:
#                     print('bs',maxWidth-tc+gaps+1,gaps)
#                     avg_gap = (maxWidth-tc+gaps+1)//gaps
#                     print('gap hai bhai',avg_gap)
#                     extra = (maxWidth-tc+gaps+1)%gaps
#                     # biggap = ' '*(avg_gap+1)
#                     # justgap = ' '*avg_gap
#                     t.append((' '*(avg_gap+1)).join(words[li:li+extra+1]))
#                     t[-1]+= ' '*avg_gap+(' '*avg_gap).join(words[li+extra+1:i])
#                     print(t)

#                 li = i
#                 tc = len(v)
            
#         g = ''
#         y = words[li:]
#         for i in y:
#             if i:
#                 g+=i+' '
        
#         if len(g)>maxWidth:
#             g=g[:-1]
#         elif len(g)<maxWidth:
#             g=g+' '*(maxWidth-len(g))
        
#         t.append(g)
#         return t



