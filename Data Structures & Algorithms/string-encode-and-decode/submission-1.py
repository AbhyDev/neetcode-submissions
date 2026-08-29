class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=[]
        for s in strs:            
            cnt=len(s)            
            ans.append(str(cnt))
            ans.append("#")
            ans.append(s)
        print(ans)
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        strs=[]
        i=0
        start=0
        while(i<len(s)):
            while(s[i]!='#'):
                i+=1
            cnt=int(s[start:i])
            i+=1
            word=s[i:i+cnt]
            i=i+cnt
            start=i
            strs.append(word)
        return strs
        