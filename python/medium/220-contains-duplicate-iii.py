from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
         4,
         0 1 2 3. 4 5. 6
        [5,1,14,1,20,10,20], k = 3, t = 3
             ^       ^
                    i - k - 1 => remove from list
         bisect left -> 10 - 3 = 7  if overlaps  left_pos != right_pos => true
         bisect right -> 10 + 3 = 13 if no overlaps  left_pos == right_pos => add new element
         [1,1,14,17]
                 23
         [1,2,0]
        """
        bst = SortedList()
        n = len(nums)
        for i in range(0, n):
            num = nums[i]
            if len(bst) > k:
                bst.discard(nums[i - k - 1])

            left_idx = bst.bisect_left(num - t)
            right_idx = bst.bisect_right(num + t)
            if left_idx != right_idx and left_idx != len(bst):
                return True

            bst.add(num)

        return False
