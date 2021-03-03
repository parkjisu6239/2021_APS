import sys
sys.stdin = open('input.txt')

def jingi(N, M ,K, people):
    # 경과 시간, 현재 붕어빵 수
    time = 0
    fishbread = 0

    # M초마다 붕어빵을 만들자
    # x초에 손님이 오면 붕어빵 주자. 손님이 왔는데 붕어빵수가 0이하이면 불가
    # 손님이 올때마다 붕어빵 수가 1개 이상이면 가능
    # N명이 오는 시간이 '자연수'가 아니라 '정수'라고 써있음... ^^ 0초에도 온다는 소리 :)

    # 붕어빵을 받은 손님 수
    OK = 0

    # 모두가 붕어빵을 받을 때까지 반복 (중간에 불가능한 경우는 바로 RETURN)
    while OK < N:
        # 예약손님 리스트 순회
        for i in range(len(people)):
            # 현재 시간에 손님이 왔는데
            if people[i] == time:
                # 붕어빵이 있으면
                if fishbread:
                    # OK +1, 붕어빵을 주자
                    OK += 1
                    fishbread -= 1
                # 붕어빵이 없으면 'Impossible'
                else:
                    return 'Impossible'

        # 0초에오는 손님때문에 위 반복문을 먼저 하고, 아래에서 시간을 더한다.
        # 처음엔 이걸 위에다 뒀더니 997개 맞고 3개 틀림

        # 1초씩 시간이 흐른다.
        time += 1
        # M초가 되면 붕어빵 K개 만들기
        if time % M == 0:
            fishbread += K

    # OK가 N이 되어서 모든 사람들한테 붕어빵을 줬으면 가능!
    return 'Possible'


for tc in range(1, int(input())+1):
    # 예약된 손님 수, M초동안 k개 생산
    N, M ,K = map(int, input().split())
    # 정렬이 안되어 있다!!!!
    people = list(map(int, input().split()))
    print('#{} {}'.format(tc, jingi(N, M ,K, people)))



