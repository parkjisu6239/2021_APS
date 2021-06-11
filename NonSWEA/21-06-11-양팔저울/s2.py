import sys
sys.stdin = open('input.txt')

N = int(input())
chu = list(map(int, input().split()))

# 안쓴다, 왼쪽에 둔다, 오른쪽에 둔다
# 왼쪽에 두면 + 오른쪽에 두면 -로 한다 (어차피 나중에는 양쪽 차이를 계산할거니까)
# DP : 현재 idx, weight가 같다면, 뒤에 볼 필요 없다 -> 이미 나온 결과

result = set()
DP = [[0] * N for _ in range(sum(chu)+1)]

def solution(idx, weight):

    if idx == N:
        ans = abs(weight)
        if ans:
            result.add(ans)
        return

    if DP[abs(weight)][idx]:
        return

    DP[abs(weight)][idx] = 1

    solution(idx + 1, weight) # 안쓴다

    solution(idx + 1, weight + chu[idx]) # 왼쪽에 둔다

    solution(idx + 1, weight - chu[idx]) # 오른쪽에 둔다



solution(0, 0)
result = sorted(list(result))

print(len(result))
print(*result)