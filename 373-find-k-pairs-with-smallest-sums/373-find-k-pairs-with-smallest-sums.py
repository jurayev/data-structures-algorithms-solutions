from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums_one: List[int], nums_two: List[int], k: int) -> List[List[int]]:
        """
        nums1 = [1,7,11], nums2 = [2,4,6] k = 3
        
        Time O(K log K)
        Space O(K log K)
                                     
        """
        res = [] # [3,0,0] [5,0,1] [7,0,2] [9,1,0] [11,1,1] [13,2,0] [15,1,2] [15,2,1]
        i = 0
        curr = 0
        min_heap = [] #   [17,2,2]
        while len(min_heap) < k and i < len(nums_one):
            heappush(min_heap, (nums_one[i]+nums_two[0], i, 0))
            i += 1

        while min_heap and len(res) < k:
            min_val, i, j = heappop(min_heap)
            res.append([nums_one[i], nums_two[j]])
            if j+1 >= len(nums_two):
                continue
            heappush(min_heap, (nums_one[i]+nums_two[j+1], i, j+1))

        return res
