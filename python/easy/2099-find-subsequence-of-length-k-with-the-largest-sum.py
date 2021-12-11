class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
        #  0 1 2 3
        # [3,4,3,3]  k = 2 => [3,4]
        # [3,4,3,3]  k = 4 => [3,4,3,3]

        Question from Biweekly Contest 67
        """
        indexes = [(i, num) for i, num in enumerate(nums)]

        s_nums = sorted(indexes, key=lambda x: x[1])[-k:]

        out = sorted(s_nums, key=lambda x: x[0])
        return [num for i, num in out]
