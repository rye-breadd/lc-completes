"""
s1 = "abc", s2 = "lecabee"
len(s2) = 7

s1_d = {a: 1, b: 1, c: 1}
s2_d = {e: 1, c: 1, a: 1}
same = 2

l = 1
r = 4
left = e
right = b


"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_len = len(s1)
        s1_d = {}
        s2_d = {}
        same = 0
    
        for c in s1:
            s1_d[c] = s1_d.get(c, 0) + 1

        for i in range(s1_len):
            val = s2[i]
            s2_d[val] = s2_d.get(val, 0) + 1

        same = sum(1 for char in s1_d if s2_d.get(char, 0) == s1_d[char])

        if same == len(s1_d):
            return True

        l = 0
        for r in range(s1_len, len(s2)):
            left = s2[l]
            right = s2[r]
            
            if left in s1_d and s2_d[left] == s1_d[left]:
                same -= 1  # Subtracting 1 will break this exact match

            s2_d[left] -= 1

            # After decrementing: did we just form a match?
            if left in s1_d and s2_d[left] == s1_d[left]:
                same += 1  # We dropped down from having too many to exact match

            if right in s1_d and s2_d.get(right, 0) == s1_d[right]:
                same -= 1  

            s2_d[right] = s2_d.get(right, 0) + 1

            if right in s1_d and s1_d[right] == s2_d[right]:
                same += 1
            
            if same == len(s1_d):
                return True
            
            l += 1
    
        return False
            

            
            

                
            

        
        