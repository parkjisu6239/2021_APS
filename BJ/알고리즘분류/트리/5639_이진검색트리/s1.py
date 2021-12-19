import sys

sys.stdin = open('input.txt')
input = sys.stdin.readlines


tree = list(map(int, input()))


def solution(start, end):
    if start > end:
        return

    div = end + 1

    for i in range(start + 1, end + 1):
        # 루트 보다 큰 지점 --> 오른쪽 서브 트리
        if tree[start] < tree[i]:
            div = i
            break

    solution(start + 1, div - 1)
    solution(div, end)
    print(tree[start])


solution(0, len(tree) - 1)
