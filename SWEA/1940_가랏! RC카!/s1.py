import sys
sys.stdin = open("input.txt")

def GoRC(n, command):
    speed = 0 # 현재 속도
    m = 0 # 이동 거리

    for time in range(n):
        if len(command[time]) == 1: # 현재속도 유지
            m += speed # 현재속도만큼 이동
            continue
        else:
            if command[time][0] == 1: # 가속
                speed += command[time][1]
            else: # 감속
                if speed - command[time][1] <= 0: # 속도가 0보다 작아지면 0
                    speed = 0
                else:
                    speed -= command[time][1] # 아니면 감속

        # 속도 결정되었으면, Go!
        m += speed

    return m


for tc in range(1, int(input())+1):
    command = []
    # 0 하나만 들어와도 split 잘 동작함
    n = int(input())
    for i in range(n):
        command.append(list(map(int, input().split())))
    print('#{} {}'.format(tc, GoRC(n, command)))