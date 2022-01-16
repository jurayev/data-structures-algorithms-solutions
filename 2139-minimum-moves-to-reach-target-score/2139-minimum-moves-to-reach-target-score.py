class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        """
        Q2 from Weekly contest 276
        Submission time: 0:25:03
        Time spent: 10 mins + 5 mins penalty(TLE)
         
        Time Complexity: O(D), where D is the number of doubles
        """
        moves = 0
        while maxDoubles and target > 1:
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            moves += 1
        return moves + target - 1