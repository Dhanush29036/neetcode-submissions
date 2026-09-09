class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l,r=[0]*n,[0]*n
        l[0]=height[0]
        r[-1]=height[-1]
        s=0
        for i in range(1,n):
            l[i]=max(l[i-1],height[i])
            r[n-i-1]=max(r[n-i],height[n-i-1])
        for i in range(1,n-1):
            s+=min(r[i],l[i])-height[i]
        return s