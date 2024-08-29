class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = []
        for i in range(numRows):
            rows.append([])
        print(rows)
        flip = 1
        c_list = 0

        if numRows<2:
            return s

        for i in s:
            print(c_list)
            rows[c_list].append(i)
            c_list+=flip
            if c_list in [0,numRows-1]:
                flip*=-1
            
        
        t = ''
        for i in rows:
            t += ''.join(i)
        return t


        