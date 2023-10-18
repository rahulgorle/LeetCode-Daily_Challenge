from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Create an adjacency list to represent prerequisites
        graph = defaultdict(list)
        indegree = [0] * n
        
        # Build the adjacency list and indegree array
        for prev, next in relations:
            graph[prev - 1].append(next - 1)
            indegree[next - 1] += 1
        
        # Initialize a queue for topological sorting
        queue = deque()
        
        # Initialize an array to store the earliest completion time for each course
        completion_time = [0] * n
        
        # Initialize the maximum time needed to complete all courses
        max_time = 0
        
        # Enqueue courses with no prerequisites
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                completion_time[i] = time[i]
                max_time = max(max_time, completion_time[i])
        
        # Perform topological sorting
        while queue:
            course = queue.popleft()
            for next_course in graph[course]:
                indegree[next_course] -= 1
                completion_time[next_course] = max(completion_time[next_course], completion_time[course] + time[next_course])
                max_time = max(max_time, completion_time[next_course])
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        return max_time
