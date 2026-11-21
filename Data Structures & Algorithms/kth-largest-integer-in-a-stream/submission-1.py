"""
    5
7        6

"""

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k

        for n in nums:
            if len(self.h) < self.k:
                heapq.heappush(self.h, n)
            elif self.h[0] < n:
                heapq.heappop(self.h)
                heapq.heappush(self.h, n)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
                heapq.heappush(self.h, val)
        elif self.h[0] < val:
            heapq.heappop(self.h)
            heapq.heappush(self.h, val)
        return self.h[0]
        
        
        
        
