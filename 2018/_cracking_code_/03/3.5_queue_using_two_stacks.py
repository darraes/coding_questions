class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            return None

        value = self.top.value
        self.top = self.top.next

        return value

    def peek(self):
        if not self.top:
            return None

        value = self.top.value
        return value

class MyQueue:
    def __init__(self):
        self.store = Stack()
        self.operator = Stack()

    def enqueue(self, value):
        cur = self.store.pop()
        while cur is not None:
            self.operator.push(cur)
            cur = self.store.pop()

        self.store.push(value)

        rev = self.operator.pop()
        while rev is not None:
            self.store.push(rev)
            rev = self.operator.pop()

    def dequeue(self):
        return self.store.pop()


queue = MyQueue()
for i in range(5):
    print "enqueue ", i
    queue.enqueue(i)

print "......"

v = queue.dequeue()
while v is not None:
    print "dequeue ", v
    v = queue.dequeue()
