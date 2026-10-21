"""
1,2,1
1,1,2

1,1,2


"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(arr, idx):
            res.append(arr[:])
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                
                arr.append(nums[i])
                dfs(arr, i + 1)
                arr.pop()

        dfs([],0)
        return res            


        