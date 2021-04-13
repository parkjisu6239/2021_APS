import sys
sys.stdin = open('input.txt')


def hex_to_binary(N):
    float_num = N
    temp = []
    # 일반적인 2진법 구하는 방식
    for i in range(-1, -13, -1):
        # 2^-i 보다 크거나 같으면, 1적고 그만큼 빼주기
        if float_num >= 2**i:
            temp.append('1')
            float_num -= 2**i
        # 작으면 그건 없는거, 0 적기
        else:
            temp.append('0')

        # 0이 되었으면 2진 변환 완료니까 리턴 끝
        if float_num == 0:
            return ''.join(temp)

    # 12번 했는데 0 안된거면 오버플로우
    return 'overflow'


for tc in range(1, int(input())+1):
    N = float(input())
    print('#{} {}'.format(tc, hex_to_binary(N)))
