import sys
sys.stdin = open('input.txt')

que = [0] * 10000
front = 0
rear = 0

def solution(inputs):
    global front, rear
    command = inputs[0]

    if command == 'push':
        que[rear] = int(inputs[1])
        rear += 1
    elif command == 'pop':
        if rear == front:
            print(-1)
        else:
            print(que[front])
            front += 1
    elif command == 'size':
        print(rear - front)
    elif command == 'empty':
        if rear == front:
            print(1)
        else:
            print(0)
    elif command == 'front':
        print(que[front] if rear != front else -1)
    elif command == 'back':
        print(que[rear-1] if rear != front else -1)


N = int(input())
for _ in range(N):
    inputs = input().split()
    solution(inputs)