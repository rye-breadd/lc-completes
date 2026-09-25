class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        c_i = 0
        f_i = 0
        while True:
            c_i = nums[c_i]
            f_i = nums[nums[f_i]]

            if c_i == f_i:
                break # we found the cycle
        
        # finding the start of the cycle
        f_i = 0
        while True:
            c_i = nums[c_i]
            f_i = nums[f_i]

            if c_i == f_i:
                return c_i
    


    """
    c_i = 2
    f_i = 2
    """

        
