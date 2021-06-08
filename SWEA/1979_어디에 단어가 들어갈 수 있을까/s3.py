import sys
sys.stdin = open('eval_input.txt', 'r', encoding = 'UTF-8')

def Where(N, M, puzzle):
    # 단어가 들어갈 수 있는 자리 갯수
    cnt = []
    # 전치행렬 간단히 만들기!(단, 엄밀히 따지면 리스트가 아니라 리스트 안의 튜플이 됨)
    reverse_puzzle = list(zip(*puzzle))
    # 0을 기준으로 쪼개기
    for i in range(N):
        cnt.extend(''.join(map(str, puzzle[i])).split('0'))
        cnt.extend(''.join(map(str, reverse_puzzle[i])).split('0'))

    # 1이 M만큼 연속으로 나온 개수 세기
    result = 0
    for i in range(len(cnt)):
        if len(cnt[i]) == M:
            result += 1

    return result


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))
    print('#{} {}'.format(tc, Where(N, M, puzzle)))