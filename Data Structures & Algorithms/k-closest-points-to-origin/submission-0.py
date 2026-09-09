class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i in points:
            heapq.heappush(heap,[-(i[0]**2+i[1]**2)**0.5,i])
            if len(heap)>k:
                heapq.heappop(heap)
        return [i[1] for i in heap]