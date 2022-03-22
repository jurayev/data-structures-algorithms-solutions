# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nested_list: List[NestedInteger]) -> int:
        total_sum = 0
        queue = deque([(nested_list, 1)])
        while queue:
            nested_element_list, depth = queue.popleft()
            for element in nested_element_list:
                if element.isInteger():
                    total_sum += element.getInteger() * depth
                else:
                    queue.append((element.getList(), depth + 1))
        return total_sum
    
    def depthSumRecursive(self, nested_list: List[NestedInteger]) -> int:
        """
        Ideas.
        Idea 1. Recursion + depth tracking
            Time O(N)
            Space (N)
        Idea 2. Iterative BFS + level tracking
            Time O(N)
            Space (N)
        """
        return self.get_nested_sum(nested_list, 1)
        
    def get_nested_sum(self, nested_list, depth) -> int:
        curr_sum = 0
        for element in nested_list:
            if element.isInteger():
                curr_sum += element.getInteger() * depth
            else:
                curr_sum += self.get_nested_sum(element.getList(), depth + 1)
        return curr_sum
        
        