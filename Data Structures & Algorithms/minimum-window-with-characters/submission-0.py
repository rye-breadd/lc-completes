"""
XYZ

XYXZ

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        sd = {}
        td = {}
        l = 0 
        same = 0
        res = ""

        for c in t:
            td[c] = td.get(c, 0 ) + 1

        for r in range(len(s)):
            c = s[r]
            
            sd[c] = sd.get(c, 0) + 1
            
            if c in td and sd[c] == td[c]:
                same += 1
            
            while same == len(td):
                val = s[l]
                if val in td and sd[val] - 1 < td[val]:
                    if not res or (r - l + 1) < len(res):
                        res = s[l:r+1]
                    same -= 1
                sd[val] -= 1  
                l += 1
        
            

        return res
        