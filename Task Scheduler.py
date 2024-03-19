from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        max_freq = max(task_count.values())
        
        # Calculate the number of tasks with the maximum frequency
        max_freq_tasks = sum(1 for count in task_count.values() if count == max_freq)
        
        # Calculate the minimum number of intervals required without considering idle cycles
        min_intervals = (max_freq - 1) * (n + 1) + max_freq_tasks
        
        # Fill in the idle cycles if necessary
        return max(len(tasks), min_intervals)
