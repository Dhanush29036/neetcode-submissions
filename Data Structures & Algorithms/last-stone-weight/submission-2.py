class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        if len(stones)==1:
            return stones[0]
        for i in stones:
            heapq.heappush(heap,-i)
        while len(heap)>1:
            print(heap)
            a=-heapq.heappop(heap)
            b=-heapq.heappop(heap)
            if a==b:
                continue
            else:
                heapq.heappush(heap,-abs(a-b))
        if not heap:
            return 0
        else:
            return -heap[0]