class Stack:
    def __init__(self, maxSize):
        self.list = []
        self.maxSize = maxSize

    def isEmpty(self):
        if not self.list:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            False

    def push(self, value):
        if self.isFull():
            return "Stack is full"
        else:
            self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None
