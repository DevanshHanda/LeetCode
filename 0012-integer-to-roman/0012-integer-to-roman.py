class Solution:
    def intToRoman(self, num: int) -> str:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        b = {0: ["I", "V"], 1: ["X", "L"], 2: ["C", "D"], 3: ["M"]}

        n = len(str(num)) - 1
        l = [v + "0" * (n - i) for i,v in enumerate(str(num))]
        t = ""
        for i, v in enumerate(l):
            try:
                t += (b[n - i][0] * int(v[0])).replace(9 * b[n - i][0], b[n - i][0] + b[n - i + 1][0]).replace(5 * b[n - i][0], b[n - i][1]).replace(4 * b[n - i][0], b[n - i][0] + b[n - i][1])
                # print(t)     
            except:
                t += (b[n - i][0] * int(v[0]))
                # print(t)
                pass
        return t