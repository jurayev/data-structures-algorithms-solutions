class Solution:
    def countPoints(self, rings: str) -> int:
        """
        "B0B6G0R6R0R6G9"
                      ^
        
        
        """
        n = len(rings)
        mapa = {}
        for i in range(n-1, -1, -2):
            number, color = rings[i], rings[i-1]
            if number not in mapa:
                mapa[number] = {}
            mapa[number][color] = 1

        total = 0  
        for colors in mapa.values():
            total += len(colors) == 3
        return total