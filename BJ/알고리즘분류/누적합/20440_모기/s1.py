import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[1])
s, e, mosquito = 0, 0, 0

for enter, leave in arr:
    if leave == s:
        leave = e
        continue
    if enter > s:
        enter = s



    if leave < e :
        leave = e

