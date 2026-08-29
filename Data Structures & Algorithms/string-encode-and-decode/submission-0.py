class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=[]
        for s in strs:
            ls=[]
            cnt=len(s)
            for i in s:
                ls.append(chr(ord(i)+1))
            ans.append(str(cnt))
            ans.append("#")
            ans.append("".join(ls))
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        ans=[]
        strs=[]
        i=0
        while(i!=len(s)):
            start=i
            while(s[i]!='#'):
                i+=1
            cnt=int(s[start:i])
            j=i+1
            i+=(cnt)
            strs.append(s[j:i+1])
            i+=1          
        print(strs)
        for s1 in strs:
            ls=[]
            for i in s1:
                ls.append(chr(ord(i)-1))
            ans.append("".join(ls))
        return ans