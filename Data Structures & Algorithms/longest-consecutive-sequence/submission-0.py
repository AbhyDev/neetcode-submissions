class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        maxi=0
        for i in s:
            if i-1 in s:
                continue
            cnt=1
            while(i+1 in s):
                cnt+=1
                i+=1
            maxi=max(maxi,cnt)
        return maxi
