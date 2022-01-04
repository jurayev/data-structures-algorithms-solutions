import math


class ArrayReader:

    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    start, end = 0, 1
    while reader.get(end) < key:
        start = end
        end *= 2
    print("start:", start, "end:", end)

    while start <= end:
        mid = start + (end - start) // 2
        val = reader.get(mid)
        if val == key:
            return mid
        if val < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    print(search_in_infinite_array(reader, 26))
    print(search_in_infinite_array(reader, 30))
    print(search_in_infinite_array(reader, 32))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))


main()
