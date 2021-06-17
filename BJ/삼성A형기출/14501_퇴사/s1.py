import sys
sys.stdin = open('input.txt', 'r')
q = lambda: map(int, sys.stdin.readline().split())

# 설계
# i일째에 일을 할지 or 안할지 -> 2가지 경우
# i일째까지 일을 했는데, DP[i]보다 작은 경우 -> 백트래킹
# 종료일이 퇴사 이후인 경우 -> 백트래킹

# ---------------------- 구현 ------------------------- #
def consulting(day, money):
    global MAX
    if day == N:
        MAX = max(MAX, money)
        return

    if day > N:
        return

    if money < DP[day]:
        return

    DP[day] = money

    consulting(day + arr[day][0], money + arr[day][1]) # 일 하는 경우
    consulting(day + 1, money) # 일 안하는 경우


# ---------------------- 입력 ------------------------- #
N = int(input())
arr = [list(q()) for _ in range(N)]


# ---------------------- 준비 ------------------------- #
DP = [0] * N # DP[i] i일까지 벌 수 있는 돈의 최댓값
MAX = 0 # 최대값


# ---------------------- 실행 ------------------------- #
consulting(0, 0)
print(MAX)