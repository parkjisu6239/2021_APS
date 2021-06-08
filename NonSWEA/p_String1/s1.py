import sys
sys.stdin = open('eval_input.txt', 'r', encoding = 'UTF-8')

def howmanypattern(pattern, text):
    # 인덱스접근
    cnt = 0
    # 구간합 범위 구하는 것과 동일
    for i in range(len(text)-len(pattern)+1):
        j = 0
        while j < len(pattern):
            if text[i+j] == pattern[j]:
                j += 1
            else:
                break
        else:
            cnt += 1
    return cnt



for _ in range(1, 11):
    tc, pattern, text = input(), input(), input()
    print('#{} {}'.format(tc, howmanypattern(pattern, text)))
