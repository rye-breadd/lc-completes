"""

          (
      ((    () 
  ((( (()

can only close a parantheses if there are more ( that exist 

res = ()
left_total = 0
total = 1
arr = ()


"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(arr, left_total, total):
            if total == n:
                res.append("".join(arr))
                return

            if left_total > n:
                return
            
            # add one more paren
            left_total += 1
            arr.append("(")
            backtrack(arr, left_total, total)
            arr.pop()
            left_total -= 1
    
            # finish it
            if left_total > total:
                arr.append(")")
                backtrack(arr, left_total, total + 1)
                arr.pop()
            
        backtrack([], 0, 0)
        return res

            
            
            


        