class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        c = '{0:b}'.format(c)
        a = '{0:b}'.format(a)
        b = '{0:b}'.format(b)

        # print(a,b,c)

        lc,la,lb = len(c),len(a),len(b)
        m = max(la,lb,lc)
        a='0'*(m-la)+a
        b='0'*(m-lb)+b
        c='0'*(m-lc)+c

        # and 1 => both need to be 1
        # or 0 => both need to be 1 
        bmp=0

        print(a,b,c)
        for i in range(m):
            if c[i]=='1':
                if int(a[i])+int(b[i])>0:
                    continue
                else:
                    bmp+=1
            elif c[i]=='0':
                if int(a[i])+int(b[i])==0:
                    continue
                elif int(a[i])+int(b[i])==1:
                    bmp+=1
                    # print('ye ni hua')
                    # continue
                else:
                    bmp+=2
                    # print('hua')
        return bmp



        

        