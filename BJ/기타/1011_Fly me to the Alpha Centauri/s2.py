import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def solution(loca, cnt, d):
    global result
    if loca >= y-1:
        if loca == y-1:
            result = min(result, cnt)
        return

    if d <= 0:
        return

    if cnt > result:
        return

    solution(loca + d - 1, cnt + 1, d-1)
    solution(loca + d, cnt + 1, d)
    solution(loca + d + 1, cnt + 1, d + 1)



for _ in range(int(input())):
    x, y = map(int, input().split())
    result = 987654321

    solution(x+1, 2, 1)

    print(result)
