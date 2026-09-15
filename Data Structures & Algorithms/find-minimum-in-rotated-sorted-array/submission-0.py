"""
Find if you are on the rotating side?

[1,2,3,4]
[4,1,2,3]

if the middle < right --> on the non rotated side --> go left

[3,4,1,2]
[2,3,4,1]

if the middle > right --> on the rotated side --> go right

[1,2,3]
[3,1,2]
[2,3,1]


middle is larger than the right


 [3,4,5,6,1,2]

left < mid go right
mid < right go left
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums[0] <= nums[(0 + len(nums) - 1) // 2] <= nums[-1]:
            return nums[0]

        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]
            
            
        