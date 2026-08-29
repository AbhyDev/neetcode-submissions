from heapq import heappush, heappop, heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        ls=[]
        for i in d:
            ls.append([-d[i],i])
        heapify(ls)
        ans=[]
        for i in range(k):
            ans.append(heappop(ls)[1])
        return ans
