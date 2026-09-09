from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for r in range(len(nums)):
            right_val = nums[r]
            while q and right_val > nums[q[-1]]:
                q.pop()

            q.append(r)
            
            while q and q[0] <= r - k:
                q.popleft()
            
            if r >= k - 1:
                res.append(nums[q[0]])
        
        return res
    
"""
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6

q = [4]
res = [2]
"""




        