class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.insert(0,item)

    def is_empty(self):
        return self.stack == []

    def pop(self):
        if self.is_empty():
            return "Stack Empty"
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

    def reverse(self):
         while True:
             if len(self.stack) == 0:
                 break
             else:
                print(self.stack.pop(0))



s1 = Stack()
s1.push("Cat")
s1.push("Dog")
s1.push("Bird")
s1.push("fish")
print(s1.size())
print(s1.peek())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())

s1.push("C")
s1.push("a")
s1.push("t")
s1.reverse()






