import sys
sys.stdin = open('input.txt', 'r')
q = lambda: map(int, sys.stdin.readline().split())

# 설계
# 4가지 연산자 중 택 1 -> 완탐, 재귀
# idx까지의 결과가 같고, 남은 연산자 상태도 같은 경우 -> 백트래킹

# ---------------------- 구현 ------------------------- #
def calculation(a, b, oper): # 연산
    if oper == 0:
        return a + b
    elif oper == 1:
        return a - b
    elif oper == 2:
        return a * b
    else:
        if a < 0 or b < 0:
            return -(abs(a) // abs(b))
        else:
            return a // b


def solution(idx, total): # 재귀
    global MAX, MIN

    if idx == N:
        MAX = max(MAX, total)
        MIN = min(MIN, total)
        return

    if visit.get((idx, total, *operator), 0):
        return

    visit[(idx, total, *operator)] = 1

    for i in range(4):
        if operator[i]:
            operator[i] -= 1
            solution(idx+1, calculation(total, nums[idx], i))
            operator[i] += 1


# ---------------------- 입력 ------------------------- #
N = int(input())
nums = list(q())
operator = list(q()) # + - * /


# ---------------------- 준비 ------------------------- #
MAX, MIN = -9999999999, 9999999999
visit = dict()


# ---------------------- 실행 ------------------------- #
solution(1, nums[0])
print(MAX)
print(MIN)