class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        """
        [[10,50],[60,120],[140,210]]
                   ^
        [[0,15],[60,70]]
                   ^
        
        [[0,15,0], [10,50,1],[40,70,0],[60,120,1],[140,210,1]]
           
        dur 10
        [[0,70,0]]
        """
        
        slots1.sort()
        slots2.sort()
        
        p1 = 0
        p2 = 0
        
        while p1 < len(slots1) and p2 < len(slots2):
            
            start, end = max(slots1[p1][0], slots2[p2][0]), min(slots1[p1][1], slots2[p2][1])
            diff = end - start
            if diff >= duration:
                return [start, start+duration]
            if slots1[p1][1] < slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return []