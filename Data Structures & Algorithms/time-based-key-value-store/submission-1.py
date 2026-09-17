"""
{
 1: [(1,dog),(3,cat)]
 2:
}


get

binary search of leftmost boundary

get 3    
[0,2,4,9,12]

if number == target --> return taht
number higher than target --> r = m - 1
number lowe than target --> l = m + 1
l = 2 # upperbound, return l - 1
r = 1

get 10
[0,1,3,4,6,7]
"""
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        k_arr = self.keys[key]
        if not k_arr:
            return ""

        l = 0
        r = len(k_arr) - 1
        while l <= r:
            m = (l + r) // 2
            if k_arr[m][0] < timestamp:
                l = m + 1
            elif k_arr[m][0] > timestamp:
                r = m - 1
            else:
                return k_arr[m][1]
    
        
        return k_arr[l - 1][1] if k_arr[l - 1][0] < timestamp else ""
"""
[] --> ""
[1,2,3] --> 2 val
get = 2
[1,2,3,4,5]
l = 0
r = 1
m = 2
"""
            
        
