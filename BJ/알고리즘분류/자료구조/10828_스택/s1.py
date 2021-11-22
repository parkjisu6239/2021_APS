import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.arr = []

    def s_empty(self):
        if len(self.arr):
            return 0
        else:
            return 1

    def s_push(self, val):
        self.arr.append(val)

    def s_pop(self):
        if self.s_empty():
            return -1
        else:
            return self.arr.pop()

    def s_top(self):
        if self.s_empty():
            return -1
        else:
            return self.arr[-1]

    def s_size(self):
        return len(self.arr)


N = int(input())
s = Stack()

for _ in range(N):
    cmd = list(map(str, input().split()))
    if cmd[0] == "push":
        s.s_push(cmd[1])
    elif cmd[0] == "pop":
        print(s.s_pop())
    elif cmd[0] == "size":
        print(s.s_size())
    elif cmd[0] == "empty":
        print(s.s_empty())
    elif cmd[0] == "top":
        print(s.s_top())


