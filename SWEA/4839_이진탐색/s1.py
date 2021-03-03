import sys
sys.stdin = open("input.txt", "r")

def BitSelection(page, A, B):

    # 첫페이지, 마지막페이지 정의
    a_l, b_l = 1, 1
    a_r, b_r = page, page

    while True:
        # 가운데 페이지
        a_c = int((a_l + a_r) / 2)
        b_c = int((b_l + b_r) / 2)
        # 찾으려는 페이지가 가운데 기준 왼쪽에 있으면 끝점을 변경 r = c
        # 찾으려는 페이지가 가운데 기준 오른쪽에 있으면 시점을 변경 l = c
        if A < a_c:
            a_r = a_c
        else:
            a_l = a_c

        if B < b_c:
            b_r = b_c
        else:
            b_l = b_c

        # A,B 둘중에 페이지를 찾은 사람이 있으면 스탑
        if a_c == A or b_c == B:
            break

    # 둘다 동시에 찾았으면 리턴 0, 둘중에 한쪽은 찾고 나머지는 못찾으면 찾은쪽만 리턴
    if A == a_c and B == b_c:
        return 0
    elif A == a_c:
        return 'A'
    else:
        return 'B'


T = int(input())
for tc in range(1, T+1):
    page, A, B = map(int, input().split())
    print('#{} {}'.format(tc, BitSelection(page, A, B)))