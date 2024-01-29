class MyQueue:

    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def push(self, x: int) -> None:
        self.stack_enqueue.append(x)

    def transfer_elements(self):
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())

    def pop(self) -> int:
        self.transfer_elements()
        return self.stack_dequeue.pop()

    def peek(self) -> int:
        self.transfer_elements()
        return self.stack_dequeue[-1]

    def empty(self) -> bool:
        return not self.stack_enqueue and not self.stack_dequeue
