class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=nums[0]
        output=[1]*(len(nums))
        for i in range(1,n):
            output[i]=prefix
            prefix*=nums[i]
        postfix=nums[n-1]
        for i in range(n-2,-1,-1):
            output[i]*=postfix
            postfix*=nums[i]
        return output
