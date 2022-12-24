class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.minStack[-1]


minStack = MinStack()

minStack.push(0)
minStack.push(-2)
minStack.push(0)

print(f"Get Minimum: {minStack.get_min()}")  # -2

minStack.pop()
print(f"Get Top: {minStack.top()}")          # -2
print(f"Get Minimum: {minStack.get_min()}")  # -2
minStack.pop()

minStack.push(-3)
minStack.push(0)

print(f"Get Minimum: {minStack.get_min()}")  # -3
