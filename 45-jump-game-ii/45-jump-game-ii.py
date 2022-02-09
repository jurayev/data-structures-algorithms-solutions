class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        BFS Solution
         0 1 2 3 4
        [2,3,1,1,4]
        
        0: [0,1,2]
        1: [1,2,3,4]
        2: [2,3]
        3: [3,4]
        4: []
        """
        n = len(nums)

        start, end, jumps, target = 0, 0, 0, n-1

        while end < n-1:
            max_end = start
            end = min(n-1, end)
            for step in range(start, end+1):
                max_end = max(max_end, step + nums[step])
            
            start, end = end+1, max_end
            jumps += 1
        return jumps
            
            