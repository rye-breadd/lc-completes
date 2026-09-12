class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        left_boundary = [0] * len(heights)
        for l in range(len(heights)):
            h = heights[l]

            while s and h <= heights[s[-1]]:
                s.pop()
            
            if s:
                left_boundary[l] = s[-1]
            else:
                left_boundary[l] = -1
            
            s.append(l)

        s = []
        right_boundary = [len(heights)] * len(heights)
        for r in range(len(heights) - 1, -1, -1):
            h = heights[r]

            while s and h <= heights[s[-1]]:
                s.pop()
            
            if s:
                right_boundary[r] = s[-1]
            else:
                right_boundary[r] = len(heights)

            s.append(r)
    
        res = 0
        for i in range(len(heights)):
            curr_height = heights[i] * (right_boundary[i] - left_boundary[i] - 1)
            res = max(res, curr_height)
        return res

        