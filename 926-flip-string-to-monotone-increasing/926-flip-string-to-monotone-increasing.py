class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        return self.get_min_flips(s)
        
    def get_min_flips(self, bin_string):
        """
        "010110"
         011233
         222
         
        """
        size = len(bin_string)
        prefix_ones = [0 for _ in range(size+1)]

        for idx in range(0, size):
            if bin_string[idx] == "1":
                prefix_ones[idx+1] = prefix_ones[idx] + 1
            else:
                prefix_ones[idx+1] = prefix_ones[idx]
        
        flip_count = size
        for idx in range(size+1):
            zeros_count = size - idx - (prefix_ones[-1] - prefix_ones[idx])
            flip_count = min(flip_count, prefix_ones[idx] + zeros_count)
        # suffix_size = size - suffix_start_idx
        # total_zeros = suffix_size - total_ones
        return flip_count

