
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


        