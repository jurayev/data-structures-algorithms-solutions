class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
         1 2 3 4 5 6 7  8
        [0,1,3,5,6,8,12,17]
  run1       1 2 2   3 4  5
  run2     1 2 2 1 2
  run3     1 2   3 2   
           
        
        1. subproblems: jump(i, j, k) - reach j from i with k step
        2. recurrence:  1. jump(i, j+k, k)
                        2. jump(i, j+k+1, k+1)
                        3. jump(i, j+k-1, k-1)
        4. intial state: jump(i=0, 0+1, 1)
        3. answer: jump(n-1, n-1, k)
        
        O(2^n) - exponential
        
        O(N*K) - pseudo-linear
        """
        stone_positions = {value: index for index, value in enumerate(stones)}
        
        @lru_cache(maxsize=None)
        def can_jump(start, end, jump):
            if start >= end or end > stones[-1]:
                return False
            if end not in stone_positions:
                return False
            
            if end == stones[-1]:
                return True
            
            return can_jump(end, end+jump, jump) \
        or can_jump(end, end+jump+1, jump+1) \
        or can_jump(end, end+jump-1, jump-1) 
        """
        return jump(end, end+jump, jump) \           # jump(1, 1+1, 1) # jump(1, 2, 1)
                or jump(end, end+jump+1, jump+1) \   # jump(1, 1+1+1, 1+1) # jump(1, 3, 2)
                or jump(end, end+jump-1, jump-1)     # jump(1, 1+1-1, 1-1) # # jump(1, 1, 0)
        """
        return can_jump(0, 1, 1)