class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            ls=[0]*26
            for x in i:
                ls[ord(x)-ord('a')]+=1
            ls=tuple(ls)
            if ls in d:
                d[ls].append(i)
            else:
                d[ls]=[i]
        ans=[]
        for x in d:
            ans.append(d[x])
        return ans
