import time


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def is_empty(self):
        return self.queue == []

    def dequeue(self):
        if self.is_empty():
            return "Queue Empty"
        return self.queue.pop()

    def peek(self):
        return self.queue[len(self.queue)-1]

    def size(self):
        return len(self.queue)

    def wait_for_your_turn(self):
        while True:
            if len(self.queue) == 0:
                break
            else:
                print(f"{self.dequeue()} takes you turn")
                time.sleep(2)


q1 = Queue()
q1.enqueue("Cat")
q1.enqueue("Dog")
q1.enqueue("Bird")
q1.enqueue("fish")
print(q1.size())
print(q1.peek())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())

q1.enqueue("C")
q1.enqueue("a")
q1.enqueue("t")
q1.wait_for_your_turn()
