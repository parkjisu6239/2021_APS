import sys
sys.stdin = open('input.txt', 'r', encoding = 'UTF-8')

def howmanypattern(pattern, text):
    # 슬라이싱
    cnt = 0
    # 구간합 범위 구하는 것과 동일
    for i in range(len(text)-len(pattern)+1):
        if text[i : i + len(pattern)] == pattern:
            cnt += 1
    return cnt



for _ in range(1, 11):
    tc, pattern, text = input(), input(), input()
    print('#{} {}'.format(tc, howmanypattern(pattern, text)))
