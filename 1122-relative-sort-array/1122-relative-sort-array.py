class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        Time O(N) , N is the total elements in arr1
        Space O(K), K is the total elements in arr2
        
        """
        size = len(arr1)
        counts = collections.Counter(arr1)

        curr_index = 0
        for num in arr2:
            while counts[num] > 0:
                counts[num] -= 1
                arr1[curr_index] = num
                curr_index += 1

        for num, count in sorted(counts.items(), key=lambda x: (x[0], x[1])):
            while count > 0:
                count -= 1
                arr1[curr_index] = num
                curr_index += 1
        return arr1
