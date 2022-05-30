import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

# 조각수 = (가로로 자른 횟수 + 1) * (세로로 자른 횟수 + 1)
# 이진 탐색을 할 타겟 = 가로 횟수 or 세로 횟수

n, k = map(int, input().split())


def get_pieces(vertical):
    return (vertical + 1)*(n - vertical + 1)


def bs(s, e):
    if e < s:
        print('NO')
        return

    m = (s + e)//2
    pieces = get_pieces(m)
    if pieces == k:
        print('YES')
        return
    elif pieces < k:
        bs(m+1, e)
    else:
        bs(s, m-1)


bs(0, n//2)
