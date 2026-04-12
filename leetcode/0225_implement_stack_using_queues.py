# Easy 
# Stack - Queue

# Using 1 Queue
# O(n) Time for push, O(1) Time for pop, top and empty
# O(n) Space, where n is the number of elements in the stack
from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()






# Efficient Implementation using a single list but violates the problem constraint of using only queue operations
# O(1) Amortized Time for push, pop and top. O(1) Time for empty 
# O(1) Time for pop, top and empty

# class MyStack:

#     def __init__(self):
#         self.stack = []
        

#     def push(self, x: int) -> None:
#         self.stack.append(x)

#     def pop(self) -> int:
#         return self.stack.pop()
        

#     def top(self) -> int:
#         return self.stack[-1]

#     def empty(self) -> bool:
#         return len(self.stack) == 0


# # Your MyStack object will be instantiated and called as such:
# # obj = MyStack()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.empty()