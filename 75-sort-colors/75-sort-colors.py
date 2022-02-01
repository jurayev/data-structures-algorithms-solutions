class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Time O(N + M), N is the total nums, M is the total unique colors == 3
        Space O(M)
        """
        self.counting_sort(nums)
        
    def counting_sort(self, nums):
        buckets = [0] * 3
        for num in nums:
            buckets[num] += 1

        running_idx = 0
        for bucket_num in range(len(buckets)):# O(m + n)
            count = buckets[bucket_num]
            for i in range(0, count):
                nums[running_idx] = bucket_num
                running_idx += 1
        return nums

        