from collections import deque, defaultdict

def dfs(sources, graph, indegree, sorted_order, orders):
  for source in sources:
      next_sources = sources[:]
      next_sources.remove(source)
      sorted_order.append(source)
      for dest in graph[source]:
        indegree[dest] -= 1
        if indegree[dest] == 0:
          next_sources.append(dest)
      dfs(next_sources, graph, indegree, sorted_order, orders)

      for dest in graph[source]:
        indegree[dest] += 1
      sorted_order.remove(source)
  if len(sorted_order) == len(indegree):
    orders.append(sorted_order[:])

def print_orders(tasks, prerequisites):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for _from, _to in prerequisites:
        graph[_from].append(_to)
        indegree[_to] += 1
    sorted_order = []

    sources = [t for t in range(tasks) if indegree[t] == 0]
    orders = []
    dfs(sources, graph, indegree, sorted_order, orders)

    for order in orders:
      print(order)



def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
