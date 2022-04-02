class Solution:
    def findBuildings(self, buildings: List[int]) -> List[int]:
        #return self.find_buildings_with_ocean_view_sol3(buildings)
        return self.find_buildings_with_ocean_view_sol2(buildings)
    
    def find_buildings_with_ocean_view_sol3(self, buildings):
        tallest = 0
        n = len(buildings)
        buildings_with_view = []
        for index in range(n-1, -1, -1):
            height = buildings[index]
            if height > tallest:
                buildings_with_view.append(index)
                tallest = max(tallest, height)
        return buildings_with_view[::-1]
    
    def find_buildings_with_ocean_view_sol2(self, buildings):
        increasing_stack = []

        for index, height in enumerate(buildings):
            while increasing_stack and buildings[increasing_stack[-1]] <= height:
                increasing_stack.pop()

            increasing_stack.append(index)

        return increasing_stack
