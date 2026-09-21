import heapq 
from collections import Counter 
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums 
        d1 = Counter(nums)
        min_heap = []
        for e , f in d1.items():
            heapq.heappush(min_heap,(f,e))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return [e for f,e in min_heap]        
