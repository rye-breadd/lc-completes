"""
[1,2,2,4,5,6,9]



   

"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(arr, idx, total):
            if total == target:
                res.append(arr[:])
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i - 1] == candidates[i]:
                    continue
                
                if candidates[i] + total > target:
                    break

                arr.append(candidates[i])
                dfs(arr, i + 1, total + candidates[i])
                arr.pop()
        
        dfs([], 0, 0)
    
        return res
            

            


        dfs([],0,0)
        return res


        