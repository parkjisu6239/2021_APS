import sys
sys.stdin = open('input.txt', 'r', encoding = 'UTF-8')

def Cut_pipe(pipe):
    pipe_cnt = 0
    cut_cnt = 0
    for i in range(len(pipe)):
        # 여는 괄호가 나오면, 막대기 시작 or 레이저 시작
        # 둘중 어떤거 일지는 모르지만, 일단 +1
        if pipe[i] == '(':
            pipe_cnt += 1
        else:
            # 닫는 괄호가 나오면 막대기의 끝 or 레이저가 막대기를 절단
            # 둘중 뭐 일지 모르지만 일단 -1
            # (괜찮은 이유) 막대기들이 쭉 나오가다 ()를 만나면 이전까지 나온 막대기의 갯수에
            # 1을 더했다 1 빼지는 것이므로, 실제 막대기 갯수가 됨
            pipe_cnt -= 1
            # '(' 다음에 바로 ')' 가 나온 경우 = 레이저
            # 레이저가 나온 경우, 지금까지 쌓여있는 막대기를 한번에 자르니까,
            # 막대기의 갯수만큼 절단 갯수가 올라감
            if pipe[i-1] == '(':
                cut_cnt += pipe_cnt
            # 전에 나온게 ')'인 경우 = ))가 연달아 나온 경우 > 막대기의 끝점인 것
            # 막대기의 마지막 1개 부분이 끝난 것이므로 절단개수 +1
            else:
                cut_cnt += 1

    return cut_cnt



for tc in range(1, int(input())+1):
    pipe = input()
    print('#{} {}'.format(tc, Cut_pipe(pipe)))