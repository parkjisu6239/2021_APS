import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

# 대기시간 생각할 필요 X
# 심사하는데 x 시간이 걸리는 심사관이 t 시간 동안 심사할 수 있는 사람 수는 ? t // x
# 1️⃣ t 시간동안 각 심사관이 심사할 수 있는 사람의 합 ? sum(t//x1 +  t//x2 + ... + t//xn)
# 2️⃣ 총 M 명을 t 시간동안 심사할 수 있는가 ? sum(t//x1 +  t//x2 + ... + t//xn) >= M

N, M = map(int, input().split())
waiting = [int(input()) for _ in range(N)]
right = M * min(waiting) # 적당한 최대값


def isPossible(limit):
    total = 0
    for w in waiting:
        total += limit // w # 1️⃣
        if total >= M: # 2️⃣
            return True

    return False


def bs(left, right):
    if right <= left:
        return right

    m = (left + right) // 2
    if isPossible(m):
        return bs(left, m)
    else:
        return bs(m+1, right)


print(bs(1, right))
