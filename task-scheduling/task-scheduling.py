from collections import deque, defaultdict

def is_scheduling_possible(tasks, prerequisites):
      indegree = defaultdict(int)
      graph = defaultdict(list)
      for _from, _to in prerequisites:
            graph[_from].append(_to)
            indegree[_to] += 1 # increment number of inbound edges
      # find all sources with indegree == 0
      sources = deque([task for task in range(tasks) if indegree[task] == 0])
      while sources:
            source = sources.popleft()
            for dest in graph[source]:
                  indegree[dest] -= 1
                  if indegree[dest] == 0:
                        sources.append(dest)

      for node, count in indegree.items():
            if count > 0: return False
      return True


def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()
