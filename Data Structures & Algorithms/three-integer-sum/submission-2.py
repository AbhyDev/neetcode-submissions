class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        s=set()
        for i in range(n-2):
            target=-nums[i]
            j=i+1
            k=n-1
            while(j<k):
                a=nums[j]
                b=nums[k]
                if a+b==target:
                    s.add(tuple([nums[i],a,b]))
                    j+=1
                    k-=1
                elif a+b<target:
                    j+=1
                else:
                    k-=1
        
        return list(s)
