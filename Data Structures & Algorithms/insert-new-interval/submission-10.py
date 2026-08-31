class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n=len(intervals)
        L=newInterval[0]
        R=newInterval[1]
        for i in range(n):
            left=intervals[i][0]
            right=intervals[i][1]
            if L<left:
                intervals.insert(i,[L,R])
                break
            elif L==left:                
                intervals.insert(i,[L,R])
        if len(intervals)==n:
            intervals.append(newInterval)
        ans=[]
        left=intervals[0][0]
        right=intervals[0][1]
        for i in range(n+1):
            l=intervals[i][0]
            r=intervals[i][1]
            if right>=l:
                right=max(right,r)
            else:
                ans.append([left,right])
                left=l
                right=r
        ans.append([left,right])
        return ans
