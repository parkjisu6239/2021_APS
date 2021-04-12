import sys
sys.stdin = open('input.txt')


# 1. 암호의 시작 좌표 찾기
def find_pattern(code):
    for r in range(len(code)):
        if '1' in code[r]:
            for c in range(M - 6):
                # 하나만 같은지 보고 넘어갔더니 오류나서 2개 보기로 함
                if code[r][c: c + 7] in password.keys() and code[r][c+7: c + 14] in password.keys():
                    return (r, c)


# 2. 암호 해독하기
def solve_password(t):
    password_num = []
    for i in range(0, len(t), 7):
        s = t[i:i+7]
        # 딕셔너리 키값에 해당 하는 벨류
        password_num.append(password[s])
    return password_num


# 3. 암호 검증하기
def is_right(pw):
    total = 0
    check = 0
    # 홀짝 나눠서
    for i in range(len(pw)):
        if i%2:
            check += pw[i]
        else:
            check += pw[i]*3
        total += pw[i]

    # 검증 안되면 0, 검증되면 총합
    if check % 10:
        return 0
    else:
        return total


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]

    password = {
        '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9,
    }

    # 1. 암호의 시작 좌표 찾기
    r, c = find_pattern(code)

    # 2. 암호 해독하기
    t = code[r][c:c+56]
    pw = solve_password(t)

    # 3. 암호 검증하기
    print('#{} {}'.format(tc, is_right(pw)))