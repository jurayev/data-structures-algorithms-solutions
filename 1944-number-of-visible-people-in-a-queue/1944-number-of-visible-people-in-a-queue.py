class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        [10,6,8,5,11,9]
         
        Idea 1: Brute force from i-th pos count how many pos are smaller
        answer: count + 1
        
        
        Idea 2: 
        1. go from right to left and maintain mono descreasing stack
        1. count = len of the stack
        2. keep remving from the stack if current el is greater then top of the stack
         [10,6,8,5,11,9]
           3  1 2 1  1 0
         [11,10]
         
         if current < stack[-1]:
            count = 1
         if current > stack[-1]:
            count = len(stack)
            while stack and stack.pop()
        stack.append(current)
        
        [5,4,3,2,1]
        [5,4,3,1,0]
        
        [2]
        """
        size = len(heights)
        seen_people = [0 for idx in range(size)]
        stack = []
        for idx in range(size-1, -1, -1):
            height = heights[idx]
            seen_count = 0
            while stack and height > stack[-1]:
                seen_count += 1
                stack.pop()
            seen_people[idx] = seen_count + bool(len(stack) > 0)
            stack.append(height)
        return seen_people