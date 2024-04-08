from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = deque(students)
        sandwiches_stack = deque(sandwiches)
        
        unable_to_eat = 0
        
        while students_queue:
            # Check if the student at the front of the queue can eat the top sandwich
            if students_queue[0] == sandwiches_stack[0]:
                students_queue.popleft()
                sandwiches_stack.popleft()
                unable_to_eat = 0  # Reset unable_to_eat counter
            else:
                # If the student at the front cannot eat, move them to the end of the queue
                students_queue.append(students_queue.popleft())
                unable_to_eat += 1
                
                # If all students have tried to eat and none could, break the loop
                if unable_to_eat == len(students_queue):
                    break
        
        return len(students_queue)
