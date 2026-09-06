class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        heap=[]
        for i in c.keys():
            heapq.heappush(heap,[c[i],i])
            if len(heap)>k:
                heapq.heappop(heap)
        return [i[1] for i in heap] 
            
