import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

class Queue:
    def __init__(self):
        self.arr = [0 for _ in range(N)]
        self.front = 0
        self.rear = 0

    def q_empty(self):
        if self.front == self.rear:
            return 1
        else:
            return 0

    def q_push(self, val):
        self.arr[self.rear] = val
        self.rear += 1

    def q_pop(self):
        if self.q_empty():
            return -1
        else:
            ans = self.arr[self.front]
            self.front += 1
            return ans

    def q_front(self):
        if self.q_empty():
            return -1
        else:
            return self.arr[self.front]

    def q_back(self):
        if self.q_empty():
            return -1
        else:
            return self.arr[self.rear-1]

    def q_size(self):
        return self.rear - self.front


q = Queue()

for _ in range(N):
    cmd = list(map(str, input().split()))
    if cmd[0] == "push":
        q.q_push(cmd[1])
    elif cmd[0] == "pop":
        print(q.q_pop())
    elif cmd[0] == "size":
        print(q.q_size())
    elif cmd[0] == "empty":
        print(q.q_empty())
    elif cmd[0] == "front":
        print(q.q_front())
    elif cmd[0] == "back":
        print(q.q_back())


