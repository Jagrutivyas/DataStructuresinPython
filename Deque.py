class Deque:
    def __init__(self):
        self.deque = []

    def add_front(self,data):
        self.deque.append(data)

    def add_rear(self,data):
        self.deque.insert(0,data)

    def add_front(self,data):
        self.deque.append(data)

    def is_empty(self):
        return len(self.deque) == []

    def remove_front(self):
        if self.is_empty():
            return "Empty Deque"
        else:
            return self.deque.pop()

    def remove_rear(self):
        if self.is_empty():
            return "Empty Deque"
        else:
            return self.deque.pop(0)

    def size(self):
        return len(self.deque)

    def check_palindrome(self):
        is_palindrome = True
        while self.size() > True :
            front = self.remove_front()
            rear = self.remove_rear()
            if front != rear:
                is_palindrome = False
        return is_palindrome

d1=Deque()
d1.add_front("Dog")
d1.add_rear("cat")
d1.add_rear("Mouse")
print(f"Front :{d1.remove_front()}")
print(f"Rear :{d1.remove_rear()}")
print(f"Rear :{d1.remove_rear()}")

d2 = Deque()
word = "racecar"
for letter in word:
    d2.add_rear(letter)
print(f"Palindrome : {d2.check_palindrome()}")

d3 = Deque()
word = "racercar"
for letter in word:
    d3.add_rear(letter)
print(f"Palindrome : {d3.check_palindrome()}")
