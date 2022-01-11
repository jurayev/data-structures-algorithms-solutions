from heapq import heappop, heappush, heapify
import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = -math.sqrt(x ** 2 + y ** 2)

    def __eq__(self, other):
        return self.d == other.d

    def __lt__(self, other):
        return self.d < other.d

    def __gt__(self, other):
        return self.d > other.d

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
    result = []

    for i in range(k):
        heappush(result, points[i])

    for point in points:
        heappush(result, max(heappop(result), point))

    return result


def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
