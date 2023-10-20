from collections import deque

class NestedIterator:
    def __init__(self, nestedList):
        self.stack = deque(nestedList)
        self.current = None

    def next(self) -> int:
        return self.current

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack.popleft()
            if top.isInteger():
                self.current = top.getInteger()
                return True
            # Extend the stack with the nested list
            self.stack.extendleft(reversed(top.getList()))
        return False
