import sys
sys.stdin = open('input.txt')


def ascii_to_hex(c):
    if c.isnumeric():
        return int(c)
    else:
        hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        return hex_dict[c]


def hex_to_binary(x):
    temp = []
    # 16진수 1자리 > 2진수 4자리
    for i in range(3, -1, -1):
        val = '1' if x & (1<<i) else '0'
        temp.append(val)

    return temp


for tc in range(1, int(input())+1):
    N, asc = map(str, input().split())
    N = int(N)
    result = []
    for i in range(len(asc)):
        result.extend(hex_to_binary(ascii_to_hex(asc[i])))

    print('#{} {}'.format(tc, ''.join(result)))