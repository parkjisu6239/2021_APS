import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

# 120ms
# 재귀로 푸는 DP 문제의 대표 유형

n = int(sys.stdin.readline())
dp = [2*n] * (n+1) # dp[m] : n을 m으로 만드는 변환 횟수의 최솟값


def solution(num, cnt):
    if num == 1:  # 1이 되면 종료
        dp[num] = min(cnt, dp[num])  # 그때의 최솟값 기록
        return

    # backtracking : 더 적은 변환 횟수로 도달 가능하거나, 1로 만드는데 드는 횟수보다 이미 크면 종료
    if cnt >= dp[num] or cnt >= dp[1]:
        return

    dp[num] = cnt  # 위에서 안걸렸으면 종료

    if num % 3 == 0:
        solution(num // 3, cnt + 1)

    if num % 2 == 0:
        solution(num // 2, cnt + 1)

    solution(num - 1, cnt + 1)


solution(n, 0)
print(dp[1])