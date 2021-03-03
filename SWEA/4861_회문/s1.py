import sys
sys.stdin = open('input.txt', 'r', encoding = 'UTF-8')

def Rogguggeo(N, M, text):
    # 회문인 문장을 찾아서 담을 변수
    is_Rogguggeo = ''

    # 행 검사
    for k in range(N):
        # 구간합 범위와 마찬가지, 회문의 길이를 고려하여!
        for i in range(N-M+1):
            # 회문의 길이가 짝수, 홀수 인지 관련없이 M//2까지만 보면 확인 가능!
            for j in range(M//2):
                # 하나라도 다른게 나오면 break
                if text[k][i+j] != text[k][i+M-1-j]:
                    break
            # break안 걸리고, for문을 탈출했다는건 회문이라는 것!
            else:
                # 위에서 회문을 검사한 범위에 맞게 그 부분만 뽑기
                is_Rogguggeo = text[k][i:i+M]
                # 행에서 구해지면 그만
                if is_Rogguggeo != '':
                    return is_Rogguggeo

    # 열검사
    for k in range(N):
        for i in range(N-M+1):
            for j in range(M//2):
                if text[i+j][k] != text[i+M-1-j][k]:
                    break
            else:
                # 출력을 위해 열고정하고 행을 순회하면 글자를 한글자씩 뽑아내기!
                for l in range(i, i+M):
                    is_Rogguggeo += text[l][k]

    return is_Rogguggeo



for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    text = []
    for _ in range(N):
        text.append(input())
    print('#{} {}'.format(tc, Rogguggeo(N, M, text)))