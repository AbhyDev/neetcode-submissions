class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        d={')':'(',']':'[','}':'{'}
        for i in s:
            if i in ['(','[','{']:
                st.append(i)
            else:
                if len(st)==0:
                    return False
                if d[i]==st[-1]:
                    st.pop()
                else:
                    return False
        if st:
            return False
        return True