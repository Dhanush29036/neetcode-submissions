class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i,j=0,n-1
        m=0
        while i<j:
            m=max(m,(j-i)*min(heights[i],heights[j]))
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return m

            