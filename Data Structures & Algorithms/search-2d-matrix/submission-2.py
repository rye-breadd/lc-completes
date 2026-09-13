"""
target 10
[1,2,3],[4,5,6],[7,8,9]

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def find_num(arr):
            l = 0
            r = len(arr) - 1

            while l <= r:
                m = (l + r) // 2
                
                if arr[m] < target:
                    l = m + 1
                elif arr[m] > target:
                    r = m - 1
                else:
                    return m
            
            return -1000000
        
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            
            curr_row = matrix[m]

            if target < curr_row[0]:
                r = m - 1
            elif target > curr_row[-1]:
                l = m + 1
            else:
                # possible existence in here
                ans = find_num(curr_row)
                if ans == -1000000:
                    return False
                return True
        return False
        
        