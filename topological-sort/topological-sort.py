from collections import defaultdict, deque

# BFS (KAHN algo) SOLUTION
# Time Complexity O(V + E)
# Space Complexity O(V + E)
def topological_sort_bfs(vertices, edges):
    sortedOrder = []
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for _from, _to in edges:
        graph[_from].append(_to)
        indegree[_to] += 1

    q = deque([v for v in range(vertices) if indegree[v] == 0])
    while q:
        _from = q.popleft()
        sortedOrder.append(_from)

        for _to in graph[_from]:
            indegree[_to] -= 1
            if indegree[_to] <= 0:
                q.append(_to)
    return sortedOrder if len(sortedOrder) == vertices else []


# DFS SOLUTION
# Time Complexity O(V + E)
# Space Complexity O(V + E)
NOT_VISITED = 0
VISITING = 1
VISITED = 2


def topological_sort_dfs(vertices, edges):
    sortedOrder = []
    graph = defaultdict(list)
    states = {}
    for _from, _to in edges:
        graph[_from].append(_to)
        states[_from] = NOT_VISITED
        states[_to] = NOT_VISITED
    for vertex in range(vertices):
        dfs(vertex, graph, states, sortedOrder)
    return sortedOrder if len(sortedOrder) == vertices else []


def dfs(_from, graph, states, sorted_order):
    if states[_from] in [VISITED, VISITING]:
        return

    states[_from] = VISITING
    for _to in graph.get(_from, []):
        dfs(_to, graph, states, sorted_order)

    states[_from] = VISITED
    sorted_order.insert(0, _from)


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1], [0, 2]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [0, 5], [3, 1], [3, 2], [4, 1]])))


main()
