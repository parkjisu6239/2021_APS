import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


class Heap:
    def __init__(self, scale=1000000):
        self.arr = [0]*(scale + 1)
        self.cnt = 1

    def empty(self):
        if self.cnt == 1:
            return 1
        else:
            return 0

    def insert(self, val):
        self.arr[self.cnt] = val
        child = self.cnt
        self.cnt += 1

        parent = child // 2
        while child > 1 and self.arr[child] < self.arr[parent]:
            self.arr[child], self.arr[parent] = self.arr[parent], self.arr[child]
            child = parent

    def delete_min(self):
        if self.empty():
            return

        self.arr[1] = self.arr[self.cnt]
        self.cnt -= 1

        parent = 1
        child = parent * 2
        if child + 1 <= self.cnt and self.arr[child + 1] < self.arr[child]:
            child += 1

        while child + 1 <= self.cnt and self.arr[child] < self.arr[parent]:
            self.arr[child], self.arr[parent] = self.arr[parent], self.arr[child]
            parent = child
            child = child * 2
            if child + 1 <= self.cnt and self.arr[child + 1] < self.arr[child]:
                child += 1

    def delete_max(self):
        if self.empty():
            return

        self.cnt -= 1

    def get_result(self):
        if self.empty():
            print("EMPTY")
        else:
            print(self.arr[self.cnt - 1], self.arr[1])


T = int(input())

for _ in range(T):
    k = int(input())
    heap = Heap(k)
    for _ in range(k):
        cmd, val = map(str, input().split())
        val = int(val)
        if cmd == "I":
            heap.insert(val)
        else:
            if val == 1:
                heap.delete_max()
            else:
                heap.delete_min()
    heap.get_result()