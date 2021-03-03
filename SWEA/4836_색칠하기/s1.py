import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input())+1):
    # 색칠할 빈종이 준비 100*100
    paper = [[ 0 for _ in range(10) ] for _ in range(10)]
    colors = int(input())
    # 색이 섞인 칸의 수
    mix_cnt = 0
    for _ in range(colors):
        x1, y1, x2, y2, color = map(int, input().split())
        # (행) 왼위모서리x좌표 ~ 오아모서리x좌표 반복
        for i in range(x1, x2+1):
            # (열) 왼위모서리y좌표 ~ 오아모서리y좌표 반복
            for j in range(y1, y2+1):
                # 종이에 색칠하기, 색깔번호를 더해줌 1 or 2
                paper[i][j] += color
                # 더해지다가 3보다 커지면 빨+파 섞인거니까 섞인칸수 올리기
                if paper[i][j] == 3:
                    mix_cnt += 1
    print('#{} {}'.format(tc, mix_cnt))