class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """
        Approach:
            Find distances from left to right
            Find distances from right to left
            Find the best distance amongs "left to right" and "right to left" distances
        Time: O(N)
        Space O(N)

                    [1,0,0,0,1,0,1]
                    
                    last = 6
        
 left->right        [0,1,2,3,0,1,0]
        
 right->left        [0,3,2,1,0,1,0]
        
                    last = inf
                    [1,0,0,0]
                    [0,1,2,3]
                    [0,3,2,inf]
                    
        """
        best = 1
        n = len(seats)
        distances = [0] * n
        
        last_person = float("inf")
        # from left to right
        for i in range(0, n):
            if seats[i] == 0:
                distances[i] = abs(i - last_person)
            else:
                last_person = i
        
        last_person = float("inf")
        # from right to left
        for i in range(n-1, -1, -1):
            if seats[i] == 0:
                distances[i] = min(distances[i], abs(last_person - i))
            else:
                last_person = i
                
            best = max(best, distances[i])
        return best