import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def solution(rb):
    if ra > rb:
        max_val = ra
        min_val = rb
    elif ra < rb:
        max_val = rb
        min_val = ra
    else:
        return '1/1'

    for yaksoo in range(min_val, 0, -1):
        if min_val % yaksoo == 0 and max_val % yaksoo == 0:
            break

    return '{}/{}'.format(ra//yaksoo, rb//yaksoo)


N = int(input())
rings = list(map(int, input().split()))
ra = rings[0]

for i in range(1, N):
    print(solution(rings[i]))



