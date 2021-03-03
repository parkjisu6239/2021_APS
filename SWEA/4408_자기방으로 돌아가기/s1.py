import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    rooms = [ list(map(int, input().split())) for _ in range(N)]

    # 중첩 경로가 있으면 동시에 가지 못한다.
    # 중첩 경로는 언제 생기는가 ? 1번 학생이 [1, 4], 2번 학생이 [3, 6]이라면 2번 학생의 출발지가
    # 1번 학생의 출발~도착지 안에 있기때문에 중첩이 발생한다.
    # 여기서 3번 학생이 [5, 10] 이라 하자. 3번 학생은 2번 학생의 경로와 중첩이 있다. 하지만 1번 학생과는 없다.
    # 그렇다면 1번학생과 동시에 움직일 수 있으니, 총 시간은 2초가 걸린다.
    # 즉, n번 학생의 이동시, 1~n-1학생들의 이동경로와 중첩이 없는 경우가 1번이라도 있다면
    # 그때 그 학생과 동시에 이동하면 되고, 1초에 2명이상의 학생이 이동한다.
    # 만약 n번 학생이 앞서 있는 모든 학생들과 모두 중첩이 있다면, 앞선 학생들의 이동완료 후에 이동해야한다.


    time = 1
    for i in range(1, N):
        if rooms[i][0] < rooms[i][1]:
            i_start = rooms[i][0]
            i_end = rooms[i][1]
        else:
            i_start = rooms[i][1]
            i_end = rooms[i][0]

        for j in range(i):
            # 출발지와 도착지가 이전학생들의 출발도착지기준 왼쪽에만 있나?
            # 혹은 오른쪽에만 있나? 그런 학생이 한명이라도 있다면, 걔랑 동시에 갈 수 있다.

            if rooms[j][0] < rooms[j][1]:
                j_start = rooms[j][0]
                j_end = rooms[j][1]
            else:
                j_start = rooms[j][1]
                j_end = rooms[j][0]

            if j_start % 2 == 0: j_start -= 1
            if j_end % 2: j_end += 1


            if i_end < j_start or i_start > j_end:
                break
        else:
            time += 1

    print('#{} {}'.format(tc, time))