import sys
sys.stdin = open('input.txt')

N = int(input())
chu = list(map(int, input().split()))

# 안쓴다, 왼쪽에 둔다, 오른쪽에 둔다
# DP : 현재 idx, left, right가 같다면, 뒤에 볼 필요 없다

result = set()
DP = [[[0] * N for _ in range(sum(chu)+1)] for _ in range(sum(chu)+1)]

def solution(idx, left, right):

    if idx == N:
        ans = abs(left - right)
        if ans:
            result.add(ans)
        return

    if DP[left][right][idx]:
        return

    DP[left][right][idx] = 1

    solution(idx + 1, left, right) # 안쓴다

    solution(idx + 1, left + chu[idx], right) # 왼쪽에 둔다

    solution(idx + 1, left, right + chu[idx]) # 오른쪽에 둔다



solution(0, 0, 0)
result = sorted(list(result))

print(len(result))
print(*result)