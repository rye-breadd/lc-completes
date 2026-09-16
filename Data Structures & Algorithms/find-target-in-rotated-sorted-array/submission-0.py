"""
find rotate

[3,4,5,1,2]

middle > right
    go right by 1

[4,5,1,2,3]
left > middle
    stay
[4,5,1]

we found our inflection point
this works because finding the minimum 1 is basically our cut
since the middle > 1 we know we are on the rotated side, mdidle > 1, so a smaller number
is guarnateed on the right by 1

the left side is that we cant garuentee it since the middle can be the smallest nubmer
given by the above example, so we can stay and perform again

then we cna perform two binary searches one of the left and one on the right

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        # l = our inflection point (minimum point)
        def search(left_index, right_index):
            l = left_index
            r = right_index
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        
        # left side
        left = 0
        right = l - 1
        res = search(left, right)
        if res != -1:
            return res
        
        left = l
        right = len(nums) - 1
        res = search(left, right)
        if res != -1:
            return res
            
        return -1

        