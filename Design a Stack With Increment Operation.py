class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.increment_arr = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        index = len(self.stack) - 1
        # Apply any increment stored at this index
        popped_value = self.stack.pop() + self.increment_arr[index]
        if index > 0:
            self.increment_arr[index - 1] += self.increment_arr[index]
        self.increment_arr[index] = 0
        return popped_value

    def increment(self, k: int, val: int) -> None:
        # Only update the increment array at the k-th position
        limit = min(k, len(self.stack))
        if limit > 0:
            self.increment_arr[limit - 1] += val
