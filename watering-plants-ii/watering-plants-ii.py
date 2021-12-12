class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        """
        [2,2,4,3,3]  A = 5, B = 5  cans = 1
             1   
             2
             
             
        [1,2,4,4,5]  A = 6, B = 2  cans = 3
                      0,3    1,1 (c-(sum%c))
        
        
        """
        
        n = len(plants)
        i, j = 0, n-1
        cap_a, cap_b = capacityA, capacityB
        cans_used = 0  # 1
        
        while i < j:
            
            cans_used += cap_a < plants[i]
            cans_used += cap_b < plants[j]
            cap_a = cap_a if cap_a >= plants[i] else capacityA
            cap_b = cap_b if cap_b >= plants[j] else capacityB
            
            cap_a -= plants[i]
            cap_b -= plants[j]
            i += 1
            j -= 1
            
            
        if i == j:
            max_water = max(cap_a, cap_b)
            cans_used += max_water < plants[i]
        
        return cans_used