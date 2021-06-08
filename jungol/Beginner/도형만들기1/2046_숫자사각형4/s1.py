import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def solution_1(n):
    for i in range(1, n+1):
        for _ in range(n):
            print(i, end=" ")
        print()

def solution_2(n):
    temp = list(range(1, n + 1))
    temp_r = list(range(n, 0, -1))
    for i in range(n):
        if i % 2 == 0:
            print(*temp)
        else:
            print(*temp_r)

def solution_3(n):
    for i in range(1, n+1):
        for k in range(1, n+1):
            print(i*k, end=" ")
        print()

n, m = map(int, input().split())

if m == 1:
    solution_1(n)
elif m == 2:
    solution_2(n)
else:
    solution_3(n)


