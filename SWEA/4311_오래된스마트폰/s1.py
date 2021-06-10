import sys
sys.stdin = open('input.txt')
import time
start = time.time()

# calc: 현재까지 연산 결과, cnt: 현재까지 연산 횟수
def solution(numA, numB, operA, operB, calc, cnt):
    global Min

    if calc == target: # 타겟을 찾으면 기록
        Min = min(Min, cnt+1)
        return

    if cnt > M-1 or cnt > Min or calc > 999 or calc < 0: # 연산 범위를 벗어나거나, 횟수 초과
        return

    if cnt > visit[operA][operB][calc]: # 최소연산이 존재하면 중지
        return
    visit[operA][operB][calc] = cnt

    if operA == 0: # numA만 있는 상태 -> 숫자,문자 입력 가능
        for num in nums:
            solution(numA*10+num, numB, operA, operB, calc*10+num, cnt+1)

        for operator in operators:
            solution(numA, numB, operator, operB, calc, cnt + 1)

    elif operA and operB == 0:
        if numB == -1: # 숫자 + 오퍼레이터까지 입력된 경우 -> 숫자만 가능
            for num in nums:
                if operA == 1:
                    solution(numA, num, operA, operB, numA+num, cnt + 1)
                elif operA == 2:
                    solution(numA, num, operA, operB, numA - num, cnt + 1)
                elif operA == 3:
                    solution(numA, num, operA, operB, numA * num, cnt + 1)
                elif operA == 4 and num:
                    solution(numA, num, operA, operB, numA // num, cnt + 1)

        else: # 숫자 + 오퍼 + 미완숫자 까지 입력된 경우 -> 숫자, 오퍼 둘다 가능
            for num in nums:
                if operA == 1:
                    solution(numA, num, operA, operB, numA+num, cnt + 1)
                elif operA == 2:
                    solution(numA, num, operA, operB, numA - num, cnt + 1)
                elif operA == 3:
                    solution(numA, num, operA, operB, numA * num, cnt + 1)
                elif operA == 4 and num:
                    solution(numA, num, operA, operB, numA // num, cnt + 1)

            for operator in operators:
                solution(numA, numB, operA, operator, calc, cnt + 1)

    elif operB: # 숫 + 오 + 숫 + 오 된 경우, 숫오숫 연산 가능
        solution(calc, -1, operB, 0, calc, cnt)


for tc in range(1, int(input())+1):
    N, O, M = map(int, input().split())
    nums = (list(map(int, input().split())))
    operators = (list(map(int, input().split())))
    target_s = input()
    t_l = len(target_s)
    target = int(target_s)

    # 타겟의 모든 숫자가 입력 가능한 경우, 타겟의 길이만큼만 터치하면 성공

    # 하나라도 없으면 연산 필요!
    # 연산 최대 횟수를 1~M까지 증가시키면서 타겟으로 만들기
    # 두수, 연산자 : 1회 시행에 최대반복 횟수 -> N*N*O
    # m회(m>1) : 이전결과*N*O
    # 최대 N^(M+1)*O^M

    # 백트래킹! : 동일한 결과가 더 적은 연산으로 나온적이 있으면 중지!! -> visit
    # 연산 범위 0~999 넘으면 중지
    # 횟수가 M을 넘으면 종료

    visit = [[[M+1] * 1000 for _ in range(5)] for __ in range(5)]

    Min = 999999

    for ts in target_s:
        if int(ts) not in nums:
            for num  in nums:
                if num:
                    solution(num, -1, 0, 0, num, 1)
            if Min == 999999:
                Min = -1
            print('#{} {}'.format(tc, Min))
            break
    else:
        print('#{} {}'.format(tc, t_l))


print((time.time() - start))