class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = math.sqrt(x ** 2 + y ** 2)

class Solution:
    """
    Quick Select algo:
        Time best -> O(N)
        Time worst -> O(N^2)
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [Point(x, y) for x, y in points]
        distances = self.quick_select(distances, k)
        return [[distance.x, distance.y] for distance in distances]
        
    def quick_select(self, points, k):
        if not points:
            return []
        pivot_dist = random.choice(points)
        smaller = [point for point in points if point.dist <= pivot_dist.dist]
        bigger = [point for point in points if point.dist > pivot_dist.dist]
        
        M, N = len(smaller), len(bigger)
        
        if k == M:
            return smaller
        if k > M:
            return smaller + self.quick_select(bigger, k - M)
        return self.quick_select(smaller, k)
        