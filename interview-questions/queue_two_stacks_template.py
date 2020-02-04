class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

class Queue(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        x = self.stack2.pop()
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())
        return x

    def front(self):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        x = self.stack2.peek()
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())
        return x


if __name__ == '__main__':
    q = Queue()
    for i in range(5):
        q.enqueue(i)
    print(q.front())
    for i in range(5):
        print(q.dequeue())
