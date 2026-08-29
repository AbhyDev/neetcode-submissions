class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        ls=[]
        for i in d:
            ls.append([d[i],i])
        ls.sort(reverse=True)
        ans=[]
        i=0
        for i in range(k):
            ans.append(ls[i][1])
        return ans
