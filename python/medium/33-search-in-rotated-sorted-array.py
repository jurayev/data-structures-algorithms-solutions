class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Test-Cases:

        [4,5,6,7,0,1,2] => target = 0, answer 4
         l
                     r
        [4,5,6,7,0,1,2] => target = 3, answer -1
                     l
                     r
        [1]             => target = 0, answer -1

        [6,7,0,1,2,3,4,5] => target = 0, answer 2
         l
             r
        1. if left <= mid
                left <= target <= mid -> go left (right = mid)
                else: go right (left = mid + 1)

        2. elif mid <= right
                mid <= target <= right -> go right (left = mid)
                else: go left (right = mid-1)

        how to find pivot index: mid = left + (right-left) // 2
        """

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1

        return left if nums and nums[left] == target else -1