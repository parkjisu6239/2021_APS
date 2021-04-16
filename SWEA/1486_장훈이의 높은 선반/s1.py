import sys
sys.stdin = open('input.txt')

def solution(idx, total):
    global result
    if idx == N:
        if B <= total < result:
            result = total
        return

    if idx in visit[total]:
        return

    visit[total].append(idx)
    solution(idx+1, total + S[idx])
    solution(idx+1, total)

for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

    # 처음엔 idx-total 했더니 total이 많아서 in 확인 시간초과
    # total-idx 로 수정
    visit = [[] for _ in range(sum(S)+1)]

    result = 9999999999
    solution(0, 0)

    print('#{} {}'.format(tc, result-B))