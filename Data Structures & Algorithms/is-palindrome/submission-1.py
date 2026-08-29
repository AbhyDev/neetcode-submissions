class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while(i<j):
            if s[i]==' ' or not ('a'<=s[i]<='z' or 'A'<=s[i]<="Z" or '0'<=s[i]<='9'):
                i+=1
                continue
            if s[j]==' ' or not ('a'<=s[j]<='z' or 'A'<=s[j]<="Z" or '0'<=s[j]<='9'):
                j-=1
                continue
            a=s[i]
            b=s[j]
            if 'A'<=s[i]<='Z':
                a=chr(ord(s[i])-ord('A')+ord('a'))
            if 'A'<=s[j]<='Z':
                b=chr(ord(s[j])-ord('A')+ord('a'))
            if a!=b:
                return False
            i+=1
            j-=1
        return True
