import sys
sys.stdin = open('input.txt', 'r', encoding = 'UTF-8')

def Len_Rogguggeo(text_list):
    # 회문의 길이가 최대인걸 찾는거라, 큰것부터 찾기

    row_max_len = 0
    for len_roggu in range(100, 0, -1):
        # 행고정
        if row_max_len:
            break
        for i in range(100):
            # 열 순회, 구간합 범위
            if row_max_len:
                break
            for j in range(100-len_roggu+1):
                for k in range(len_roggu // 2):
                    if text_list[i][j + k] != text_list[i][j + len_roggu -1 -k]:
                        break
                else:
                    row_max_len = len_roggu

    col_max_len = 0
    for len_roggu in range(100, 0, -1):
        # 행고정
        if col_max_len:
            break
        for i in range(100):
            # 열 순회, 구간합 범위
            if col_max_len:
                break
            for j in range(100 - len_roggu + 1):
                for k in range(len_roggu // 2):
                    if text_list[j + k][i] != text_list[j + len_roggu - 1 - k][i]:
                        break
                else:
                    col_max_len = len_roggu

    if row_max_len > col_max_len:
        return row_max_len
    else:
        return col_max_len


for _ in range(10):
    tc = int(input())
    text_list = []
    for __ in range(100):
        text_list.append(input())
    print('#{} {}'.format(tc, Len_Rogguggeo(text_list)))