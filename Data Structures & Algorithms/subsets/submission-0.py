class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = [[]]
        def dfs(arr, idx):
            if idx >= N:
                return

            for i in range(idx, N):
                arr.append(nums[i])
                res.append(arr[:])
                dfs(arr, i + 1)
                arr.pop()
            
            return
        dfs([], 0)
        return res


        