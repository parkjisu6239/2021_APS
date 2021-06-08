import sys
sys.stdin = open("eval_input.txt", "r")

T = int(input())
prime = [2, 3, 5, 7, 11]

for tc in range(1, T+1):
    number = int(input())

    print('#{}'.format(tc), end=' ')
    for p in prime:
        cnt = 0
        # 소인수로 나누어 떨어질때만 반복, 더이상 나누어 떨어지지 않으면 cnt 출력
        while number % p == 0:
            # 소인수로 나눈값을 저장
            number = number / p
            # 횟수 +1
            cnt += 1
        print(cnt, end=' ')
    print()