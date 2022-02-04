class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Ideas:
            1. Count the frequencies, sort and take top k -> O(N) + O(N log N)
            2. heapq.nlargest -> O(N) + O(N log N)
            3. Count the frequencies and keep only top k elements in the heap -> O(N) + O(N log K)
            4. QuickSelect -> runs in O(N)
        """
        counts = collections.Counter(nums)
        counts = [item for item in counts.items()]
        
        top_k = self.quick_select(counts, k)
        return [num for num, _ in top_k]
        
    def quick_select(self, counts, k):
        """
        [(1,3), (3, 1), (2, 2)]
        
        [1,2,3,4,5]

        k = 3
        smaller = [1,2,3]
        bigger = [4,5]
        
        k = 1
        smaller = []
        bigger = [1,2,3]
        
        k = 1
        smaller = [1,2]
        bigger = [3]
        """
        pivot_idx = random.randint(0, len(counts)-1)
        pivot_count = counts[pivot_idx][1]
        smaller = [item for item in counts if item[1] < pivot_count]
        bigger = [item for item in counts if item[1] >= pivot_count]
        
        if len(bigger) == k:
            return bigger
        if len(bigger) > k:
            return self.quick_select(bigger, k)
        return bigger + self.quick_select(smaller, k-len(bigger))