class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        n=len(temperatures)
        output=[0]*(n)
        for i in range(n):
            t=temperatures[i]
            if not s:
                s.append(i)
            else:
                while(s and temperatures[s[-1]]<t):
                    a=s.pop()
                    output[a]=(i-a)
                s.append(i)
        return output