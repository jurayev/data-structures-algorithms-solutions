class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0

        running_sum = 0
        min_size = float("inf")

        while end < len(nums):
            end_num = nums[end]
            running_sum += end_num
            while running_sum >= target:
                min_size = min(min_size, end-start+1)
                start_num = nums[start]
                running_sum -= start_num
                start += 1
            end += 1

        return min_size if min_size < float("inf") else 0

        