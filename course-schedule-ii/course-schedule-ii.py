class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        {
        0: [1,2]
        1: [2]
        2: []
        }
        
        
        1.Start from every course
        2.Visit the connected course
        3. If no more courses to explore, add to the order
        4. If course in visiting courses -> cycle found -> return []
        5. Keep track of the visited and skip if visited course is found
        
        TC: O(V+E)
        SC: O(V+E)
        
        """
        colors = {"WHITE": 0, "GREY":1, "BLACK": 2}
        graph = {}
        for course in range(numCourses):
            graph[course] = []
            
        for from_node, to_node in prerequisites:
            graph[from_node].append(to_node)
        
        
        course_colors = {course: colors["WHITE"] for course in graph} 
        in_cycle = []
        order = []
        for course in range(numCourses):
            self.dfs(graph, course, colors, course_colors, order, in_cycle)
            if in_cycle: 
                return []
        return order
    
    
    def dfs(self, graph, course, colors, course_colors, order, in_cycle):
        if course_colors[course] == colors["BLACK"]:
            return
        if course_colors[course] == colors["GREY"]:
            in_cycle.append(True)
            return
        
        course_colors[course] = colors["GREY"]
        for next_course in graph[course]:
            self.dfs(graph, next_course, colors, course_colors, order, in_cycle)
        
        course_colors[course] = colors["BLACK"]
        order.append(course)