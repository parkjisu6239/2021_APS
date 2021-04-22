import sys
sys.stdin = open('input.txt')

def not_Cross(idx, c): # 대각선인가?
    for q_r in range(idx): # 앞서 선택한 행에 놓인 퀸들 확인
        q_c = sel[q_r] # (q_r, q_c)에 퀸 있음
        if abs(idx-q_r) == abs(c-q_c): # 대각선상에 위치?
            return False

    return True # 그 어떤 퀸과도 대각선에 없는 경우

def N_Queen(idx):
    global cnt

    if idx == N:
        cnt += 1 # 다 놨으면 +1

    for c in range(len(col)):
        if col[c] == 0 and not_Cross(idx, c): # 여기 놓을 수 있으면
            col[c] = 1 # 열 선택 : 0 or 1
            sel[idx] = c # 선택한 열 저장 : 실제 열번호 저장
            N_Queen(idx+1) # 다음 재귀

            # 유망하지 않아서 나온 것
            col[c] = 0 # 방문체크(아까 놓았던거 제거)


for tc in range(1, int(input()) + 1):
    N = int(input())
    col = [0] * N # col[2] = 1 일때, 2열에 퀸을 놓았다
    sel = [0] * N # sel[1] = 2 일때, (1,2)에 퀸이 있다.
    cnt = 0
    N_Queen(0)
    print('#{} {}'.format(tc, cnt))

