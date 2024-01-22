'''Data structure tutorial exercise: Stack
Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"'''

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def reverse_string(str1):
    s = Stack()
    for char in str1:
        s.push(char)
    rev_str = ''
    while s.size() != 0:
        rev_str += s.pop()
    return rev_str

if __name__ == '__main__':
    print(reverse_string("I am Indian"))
    print(reverse_string("9876543210"))