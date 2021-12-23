from heapq import heappush, heappop
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        Presort based on last day
        Skip if duration + total_time > last day for course
        
        TC: O(NlogN)
        SC: O(N)
        
        [100,200],[200,1300],[1000,1250],[2000,3200]
        
             101        1100       1300        3300
        
        [100,200],[1000,1250],[200,1300],[2000,3200]
        
        
        
        
             500       700         1700        2700
        [500,500],[200,1300],[1000,1250],[2000,3200]
        
        
        [3,3] [2,4] [2,4]  => 2
        
               ^
        time = 2 
        count = 1
         [-2]
        """
        
        sorted_courses = sorted(courses, key= lambda x: (x[1], x[0]))
        course_count = 0
        taken_courses = []
        total_time = 0
        for duration, lastday in sorted_courses:
            
            if total_time + duration <= lastday:
                course_count += 1
                total_time += duration
                heappush(taken_courses, -duration)
            elif taken_courses and -taken_courses[0] > duration:
                longer_duration = heappop(taken_courses)
                total_time += longer_duration + duration
                heappush(taken_courses, -duration)

        return course_count