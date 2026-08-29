class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new=[]
        n=len(nums)
        for i in range(n):
            new.append([nums[i],i])
        new.sort()
        ans=[]
        se=set()
        for i in range(n):
            target=-new[i][0]
            a=0
            b=n-1
            while(a!=i and b!=i):
                s=new[a][0]+new[b][0]
                if s==target:
                    se.add(tuple([new[a][0],new[i][0],new[b][0]]))
                    a+=1
                    b-=1
                elif s>target:
                    b-=1
                else:
                    a+=1
        ans=[]
        for i in se:
            ans.append(list(i))
        return ans

