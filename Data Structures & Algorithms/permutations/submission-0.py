"""
[1,2,3]

        1
    2       3
3
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        s = set()
        res = []
        def dfs(arr):
            if len(arr) == len(nums):
                res.append(arr[:])
                return

            for i in range(len(nums)):
                val = nums[i]
                if val not in s:
                    s.add(val)
                    arr.append(val)
                    dfs(arr)
                    arr.pop()
                    s.remove(val)
        dfs([])
        return res


        