class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            X=target-nums[i]
            if X in d:
                return [d[X],i]
            d[nums[i]]=i
