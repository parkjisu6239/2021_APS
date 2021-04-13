import sys
sys.stdin = open('input.txt')


def find_password(code):
    for r in range(row):
        if not code[r].isnumeric():
            return code[r].replace('0', '')


def ascii_to_hex(c):
    if c.isnumeric():
        return int(c)
    else:
        hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        return hex_dict[c]


def hex_to_binary(x):
    temp = ''
    # 16진수 1자리 > 2진수 4자리
    for i in range(3, -1, -1):
        val = '1' if x & (1<<i) else '0'
        temp += val
    return temp


for tc in range(1, int(input())+1):
    row, col = map(int, input().split())
    code = []
    for _ in range(row):
        code.append(input())

    password = find_password(code)
    print(password)
    binary = ''
    for p in password:
        binary += hex_to_binary(ascii_to_hex(p))

    print(binary, len(binary))