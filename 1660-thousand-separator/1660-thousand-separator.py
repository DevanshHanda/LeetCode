class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n/1000>=1:
            # print(n/1000)
            k = str(n)
            p = len(k)
            t=''
            i = p-3
            while i>0:
                # print(i,k[i])
                k = k[:i]+'.'+k[i:]
                # print(k)
                # i-=1

                i-=3
            # if p%3==0:
            #     return k[1:]
            # else:
            return k

        else:
            return str(n)