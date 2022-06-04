class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        [2,5,2,1,2]
        
        [1,2,2,2,5] t=5
             ^
        [122]
        [5]
        
        [10,1,2,7,6,1,5]
        [1,1,2,5,6,7,10]
        
        [1]
          [11]
            [112]
          [12]
        [1]
          [1,2]
        """
        candidates.sort()
        def generate(idx, target, curr):
            if target <= 0:
                if target == 0:
                    combs.append(list(curr))
                return
            
            prev_candidate = float("-inf")
            for idj in range(idx, len(candidates)):
                if candidates[idj] == prev_candidate:
                    continue
                curr.append(candidates[idj])
                generate(idj+1, target-candidates[idj], curr)
                curr.pop()
                prev_candidate = candidates[idj]

                
                
                
        
        combs = []
        curr = []
        generate(0, target, curr)
        
        return combs