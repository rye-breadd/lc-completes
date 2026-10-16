class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(arr, idx, total):
            if total == target:
                res.append(arr[:])
                return
          
            if idx >= len(nums) or total > target:
                return

            for i in range(idx, len(nums)):
                arr.append(nums[i])
                curr_total = nums[i] + total
                dfs(arr, i, curr_total)
                arr.pop()
        
        dfs([], 0, 0)

        return res


                
        