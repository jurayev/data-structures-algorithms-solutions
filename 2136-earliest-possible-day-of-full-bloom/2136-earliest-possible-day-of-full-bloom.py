class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """
                 012345678
        seed1        pggg
        seed2    ppppgggg
        seed3         pppg
        
        Complexity:
            Time O(nlogn)
            Space (p+g)
        """
        growt = sorted([(grow, plantTime[idx]) for idx, grow in enumerate(growTime)], reverse=True)
        
        total_plant_time = 0 # 8
        total_grow_time = 0  # 1
        for gtime, ptime in growt:
            total_grow_time = max(total_grow_time - ptime, gtime)
            total_plant_time += ptime
        
        return total_plant_time + total_grow_time