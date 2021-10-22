class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    def __init__(self):
        self.Linkedlist = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.Linkedlist]
        return ','.join(values)

    def isEmpty(self):
        if self.Linkedlist.head is None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.Linkedlist.head
        self.Linkedlist.head = node

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            nodeval = self.Linkedlist.head.value
            self.Linkedlist.head = self.Linkedlist.head.next
            return nodeval

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            nodeval = self.Linkedlist.head.value
            return nodeval

    def delete(self):
        self.Linkedlist.head = None
