class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Time Complexity - O(n)
        Space Complexity - O(1)

        [2,7,9,3,1]     => for every i check i-2 such that max (nums[i]+nums[i-2], nums[i-1]) -> take the max you can rob
                 ^

        [2,7,11,10,12]
        pp
           p
             c

        Test - Cases:
        [15,11,0, 9, 1, 0,0]
        [2,8,10,  3, 1, 1,0]
        [0,1]
        [11,1]
        [1]
        [2,7,9,3,1]
        [1,2,3,1]
        """

        prev_prev_house = nums[0]
        prev_house = max(prev_prev_house, nums[1] if len(nums) > 1 else 0)

        for i in range(2, len(nums)):
            curr_house = max(prev_prev_house + nums[i], prev_house)
            prev_prev_house = prev_house
            prev_house = curr_house
        return max(prev_prev_house, prev_house)