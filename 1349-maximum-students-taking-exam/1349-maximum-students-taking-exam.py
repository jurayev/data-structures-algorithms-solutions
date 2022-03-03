class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        """
        subproblems:
                calculate how many seats can be booked:
                    1. if take current seat
                    2. skip current seat
        recurrence:
                1. take
                2. skip
                3. book_seats(i) = for j ... n-1 
                    res = max(book_seats(i, take=True), book_seats(i, take=False))
        base cases
        Compelexity:
                Time O(2^N*4) -> 2 state per seat for n-1 seats, 4 checks per seat
                Space O(1) if input modification or O(N^2) not allowed, allocate additional space
                
        Optimize:
            1. use caching / memoization
            2. use bitmasking
            
        i-1,j-1 -> upper left
        i-1,j+1 -> upper right
        i,  j-1 -> left
        i,  j+1 -> right
        """
        max_booked = 0
        #booked = set()
        rows, cols = len(seats), len(seats[0])
        
        @lru_cache(None)
        def book_seats(r, c, curr_row_mask, prev_row_mask, count):
            nonlocal max_booked
            
            if c >= cols:
                r += 1
                c = 0
                prev_row_mask = curr_row_mask
                curr_row_mask = 0
                
            if r >= rows:
                #print("count:", count, bin(curr_row_mask), bin(prev_row_mask))
                max_booked = max(max_booked, count)
                return
            
            book_seats(r, c+1, curr_row_mask, prev_row_mask, count) # skip
            
            if seats[r][c] == "#" or curr_row_mask & (1 << max(c-1, 0)) != 0:
                return            # upper left   # upper right   # left    # right
            for ith_seat_bit in [c-1, c+1]:
                if 0 <= ith_seat_bit < cols and prev_row_mask & (1 << ith_seat_bit) != 0:
                    return
            book_seats(r, c+1, curr_row_mask | (1 << c), prev_row_mask, count+1)
        
        book_seats(0, 0, 0, 0, 0)
        return max_booked
            
            