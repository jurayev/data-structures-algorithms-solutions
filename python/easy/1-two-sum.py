class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        """
        Time complexity O(n)
        Space Complexity O(n)

        Approach: Using hasmap keep track of seen numbers.
        Examples:

        [2,7,11,15] = 17
        {2: 0
         7: 1
         11: 2
         15: 3}

        """

        for idx in range(0, len(nums)):
            num = target - nums[idx]
            if num in seen:
                return [seen[num], idx]
            seen[nums[idx]] = idx

        return [0, 1]