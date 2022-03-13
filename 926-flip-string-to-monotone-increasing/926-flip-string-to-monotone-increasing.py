class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        return self.get_min_flips(s)
        
    def get_min_flips(self, bin_string):
        """
        "010110"
         011233
         322110
         
        """
        size = len(bin_string)
        total_ones = 0
        flip_count = 0
        for idx in range(size):
            if bin_string[idx] == "1":
                total_ones += 1
            else:
                flip_count += 1
            flip_count = min(flip_count, total_ones)
        # suffix_size = size - suffix_start_idx
        # total_zeros = suffix_size - total_ones
        return flip_count

