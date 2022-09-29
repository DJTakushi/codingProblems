class Solution:
    def romanToInt(self, s: str) -> int:
        out = 0
        skip = False
        for i in range(len(s)):
            if skip ==False:
                # print("i="+str(i))
                c = s[i]
                c2 = ''
                if i < len(s)-1:
                    c2=s[i+1]
                if c=='I':
                    if c2=='V':
                        out+=4
                        skip = True
                    elif c2=='X':
                        out+=9
                        skip = True
                    else:
                        out+=1
                elif c=='V':
                    out+=5
                elif c=='X':
                    if c2=='L':
                        out+=40
                        skip = True
                    elif c2=='C':
                        out+=90
                        skip = True
                    else:
                        out+=10
                elif c=='L':
                    out+=50
                elif c=='C':
                    if c2=='D':
                        out+=400
                        skip = True
                    elif c2=='M':
                        out+=900
                        skip = True
                    else:
                        out+=100
                elif c=='D':
                    out+=500
                elif c=='M':
                    out+=1000
            else:
                skip=False
        return out

if __name__=="__main__":
    s = Solution()
    o = "fda"
    o = str(s.romanToInt("MCMXCIV"))
    print(o)
