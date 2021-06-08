import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())

def solution(n, m):

    for k in range(n):
        if k%2 == 0:
            print(*list(range(m*k+1, m*k+m+1)))
        else:
            print(*list(range(m * k + m, m * k, -1)))

solution(n, m)