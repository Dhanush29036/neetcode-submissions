class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        m=nums[0]
        a=0
        for i in range(1,len(nums)):
            m=min(nums[i],m)
            a=max(a,nums[i]-m)
        return a