class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        n=len(nums)
        for i in nums:
            d[i]=d.get(i,0)+1
        ls=[[] for _ in range(n+1)]
        for i in d:
            ls[d[i]].append(i)
        ans=[]
        for i in range(n,-1,-1):
            k-=len(ls[i])
            for x in ls[i]:
                ans.append(x)
            if k==0:
                break
        return ans