class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls1=[0]*26
        ls2=[0]*26
        for i in s:
            ls1[ord(i)-ord('a')]+=1
        for i in t:
            ls2[ord(i)-ord('a')]+=1
        return ls1==ls2