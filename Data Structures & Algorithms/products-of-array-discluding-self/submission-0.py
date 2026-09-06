class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[]
        f,b=[1]*n,[1]*n
        for i in range(1,n):
            b[i]=b[i-1]*nums[i-1]
            f[n-1-i]=f[n-i]*nums[n-i]
        for i in range(n):
            a.append(b[i]*f[i])
        return a