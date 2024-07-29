class Solution:
    def modifyString(self, s: str) -> str:
        # l = [ord(i) ]
        # print(ord('a'))

        st = ord('a')
        l= [chr(i) for i in range(st,st+26)]
        # prev = ''
        # next = ''
        
        if s.count('?')==len(s):
            return 'ac'*(len(s)//2)+'a'*(len(s)%2)
        sur = []
        # ind = 0

        for i,v in enumerate(s):
            if v=='?':
                # ind = i
                # print(v)
                if i!=0:
                    sur.append(s[i-1])
                if i!=len(s)-1:
                    sur.append(s[i+1])
                # break
        
        sedif = set(sur)
        # print(sedif)
        options = list(set(l)-sedif)
        t = options.copy()
        # print(options)
        while '?' in s:
            # print(options,options[-1])
            i = s.index('?')
            try:
                s=s[:i]+options[-1]+s[i+1:]
            except:
                options[:] = t.copy()
                s=s[:i]+options[-1]+s[i+1:]

            options.pop()
            # print(options)
        # print(s)

        return s