import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    # 소인수인지 판별한 숫자들
    num_list = [2, 3, 5, 7, 11]
    # 위 소인수의 갯수가 5개니까 각 숫자의 갯수를 셀
    # num_cnt도 0을 다섯개로 초기화
    num_cnt = [0] * 5
    # 숫자를 받음
    N = int(input())

    # 일단 tc 번호부터 출력함
    print('#{}'.format(tc), end=' ')
    # 위 소인수만큼만 보면 되고, 그때의 인덱스 필요하니까 i
    for i in range(5):
        # 각 소인수로 더이상 나누어떨어지지 않을때까지 나누기
        while N % num_list[i] == 0:
            num_cnt[i] += 1
            N //= num_list[i]
        # 최대로 나눠져서 몇제곱인지 구해지면 프린트
        print(num_cnt[i], end=' ')
    # 다음 테케가 다음줄에 나와야 되니까 프린트
    print()


