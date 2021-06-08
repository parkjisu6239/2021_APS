import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

def solution(n):
    for i in range(1, n+1):
        for j in range(n):
            print(i + n*j, end=" ")
        print()

solution(n)