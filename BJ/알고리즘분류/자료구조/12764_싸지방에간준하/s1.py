# coding=utf-8
import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
waiting = []
for _ in range(N):
    start, end = map(int, input().split())
    waiting.append((start, end))

waiting.sort()

ssazibang = []
seats = []
result = [0] * (N+1)
max_no = 1
for start, end in waiting:
    while ssazibang and ssazibang[0][0] <= start: # 앉을 자리가 있는 경우(여러개 일 수 있음)
        _, no, __ = heappop(ssazibang) # 자리 비우기
        heappush(seats, no) # 빈자리 힙에 넣기

    if seats: # 빈자리가 있는 경우
        empty_seat = heappop(seats) # 빈자리 중 작은 번호
        heappush(ssazibang, (end, empty_seat, start)) # 빈자리에 앉게 하기
        result[empty_seat] += 1 # 카운트
    else: # 앉을자리 없는 경우, 새자리 만들기
        heappush(ssazibang, (end, max_no, start))
        result[max_no] = 1
        max_no += 1

print(len(result[1: max_no]))
print(" ".join(map(str, result[1: max_no])))

# 처음에 빈자리가 있을 때 한개만 pop 했더니 틀렸다.
# 다른 풀이 보니까 while 이 있어서 왜 저게 필요하지? 생각하다보니 틀린걸 알았다.
# 새로운 사람이 왔는데 빈자리가 여러개라면 그걸 일단 다 빼줘야한다. 아니면 빈자리가 있음에도 앉지 않는 경우가 생긴다.
# 빈자리를 관리할 힙을 따로 만들어서 수정했더니 성공!
