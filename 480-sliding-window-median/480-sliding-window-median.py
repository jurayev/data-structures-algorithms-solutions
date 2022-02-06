from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        [1,3,-1,-3,5,3,6,7], k = 3
        
        [-1,1,3]
            [-3,-1,3]
                [-3,-1,3, 4]
        """
        s_list = SortedList()
        n = len(nums)
        for idx in range(0, min(k, n)):
            s_list.add(nums[idx])

        medians = []

        self.add_median(medians, s_list, k)
        for idx in range(k, n):
            s_list.discard(nums[idx-k])
            s_list.add(nums[idx])

            self.add_median(medians, s_list, k)
        return medians

    def add_median(self, medians, s_list, k):
        mid_idx = k // 2
        if self.is_odd(k):
            medians.append(s_list[mid_idx])
        else:
            medians.append((s_list[mid_idx] + s_list[mid_idx-1]) / 2)

    def is_odd(self, k):
        return k % 2 == 1
