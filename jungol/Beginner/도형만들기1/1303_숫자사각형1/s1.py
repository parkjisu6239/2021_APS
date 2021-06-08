import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())

def solution(n, m):

    for i in range(1, n*m + 1):
        print(i, end=" ")
        if i % m == 0:
            print()

solution(n, m)