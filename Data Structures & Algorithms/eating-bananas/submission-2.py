
"""

piles = [25,10,23,4], h = 4

bph = [1,2,....25]
l = 13
r = 24

m = 12

k = 
res = 5


"""



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bph = max(piles)

        def can_eat(k):
            res = 0
            for p in piles:
                res += math.ceil(p / k)

            if res <= h:
                return True
            return False

        l = 1
        r = bph

        while l <= r:
            m = (r + l) // 2

            if can_eat(m):
                r = m - 1
            else:
                l = m + 1
        return l


"""
We can do binary search with the numbers, we dont always have to do it by array. 
Next time if we can see that we are only looking at numbers that are sequential, then binary search on the numbers instead of an array is a better solution because
it is not an array of items its just a number line that we can easily repliocate just by numbers.

"""

        