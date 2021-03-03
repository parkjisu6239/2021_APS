import sys
sys.stdin = open('input.txt', 'r', encoding = 'UTF-8')

def Typing(text, pattern):
    N = len(text)
    M = len(pattern)
    quick_typing = 0
    i = 0
    while i < N-M+1:
        for j in range(M):
            # 패턴과 다르다면 반복 종료하고, 인덱스 넘기기
            if text[i+j] != pattern[j]:
                break
        # break되지 않고 완료되면, 패턴과 같다!
        else:
            # 등장횟수 늘리고, 다음 탐색은 M만큼 이동하자!
            quick_typing += 1
            # 밑에서 i를 전체적으로 올려주고 있으니, 여기서는 -1로 맞춰주기
            i = i+M-1
        i += 1


    return N - (M-1)*quick_typing


for tc in range(1, int(input())+1):
    A, B = map(str, input().split())
    print('#{} {}'.format(tc, Typing(A, B)))