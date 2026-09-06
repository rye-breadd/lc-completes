"""
s="AABABBA"
k=1

freq = {
    A: 3
    B: 2
}
max_c = 1
res = 0
l = 0

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_c = 0
        res = 0
        
        l = 0
        for r in range(len(s)):
            letter = s[r]
            freq[letter] = freq.get(letter, 0) + 1
        
            max_c = max(freq.values())
            
            window_len = (r - l) + 1

            if window_len - max_c <= k:
                res = max(res, window_len)
            
            while window_len - max_c > k:
                freq[s[l]] -= 1
                l += 1
                window_len = (r - l) + 1

        return res
        
            
        