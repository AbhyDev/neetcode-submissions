class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new=[]
        n=len(position)
        for i in range(n):
            new.append([position[i],speed[i]])
        new.sort()
        s=[]
        for i in range(n):
            a=target-new[i][0]
            b=new[i][1]
            time=a/b            
            while(s and s[-1]<=time):
                s.pop()
            s.append(time)

        return len(s)

