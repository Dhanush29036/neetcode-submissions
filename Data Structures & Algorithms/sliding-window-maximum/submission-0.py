class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r=0,k-1
        heap=[]
        for i in range(k-1):
            heapq.heappush(heap,[-nums[i],i])
        n=len(nums)
        ans=[]
        while r<n:
            heapq.heappush(heap,[-nums[r],r])
            while heap[0][1]<l:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
            r+=1
            l+=1
        return ans