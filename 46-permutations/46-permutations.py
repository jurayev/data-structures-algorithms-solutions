class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.find(nums.copy(), 0, result)
        return result

    def find(self, nums, start, result):
        if start >= len(nums):
            result.append(nums.copy())
            return

        for end in range(start, len(nums)):
            self.swap(start, end, nums)
            self.find(nums, start+1, result)
            self.swap(start, end, nums)

    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]