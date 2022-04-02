class Solution:
    def findBuildings(self, buildings: List[int]) -> List[int]:
        tallest = 0
        n = len(buildings)
        buildings_with_view = []
        for index in range(n-1, -1, -1):
            height = buildings[index]
            if height > tallest:
                buildings_with_view.append(index)
                tallest = max(tallest, height)
        return buildings_with_view[::-1]
