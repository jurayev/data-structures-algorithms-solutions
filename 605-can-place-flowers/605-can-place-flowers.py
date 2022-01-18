class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Time O(N)
        Space O(1)
        """
        l = len(flowerbed)
        for i in range(0, l):
            left = flowerbed[i-1] if i-1 >= 0 else 0
            right = flowerbed[i+1] if i+1 < l else 0
            
            if flowerbed[i] == 0 and left == flowerbed[i] == right:
                n -= 1
                flowerbed[i] = 1
                
        return n <= 0
        