import sys
sys.stdin = open('input.txt')

def jingi(N, M ,K, people):
    # 경과 시간, 현재 붕어빵 수
    time = 0
    fishbread = 0

    # M초마다 붕어빵을 만들자
    # x초에 손님이 오면 붕어빵 주자. 손님이 왔는데 붕어빵수가 0이하이면 '불가'
    # 손님이 왔을 때 붕어빵 수가 1개 이상이면 '가능'

    # 붕어빵을 받은 손님 수
    OK = 0

    # 모두가 붕어빵을 받을 때까지 반복 (중간에 불가능한 경우는 바로 RETURN)
    while OK < N:
        # 1초씩 시간이 흐른다.
        time += 1
        # M초가 되면 붕어빵 K개 만들기
        if time % M == 0:
            fishbread += K

        # 현재 시간에 손님이 왔는데
        if time == people[0]:
            # 붕어빵 줄 수 있으면 OK +1, 붕어빵을 주자
            if fishbread:
                OK += 1
                fishbread -= 1
                people.pop(0)
                break
            # 줄 붕어빵이 없으면 'Impossible'
            else:
                return 'Impossible'

    return 'Possible'



for tc in range(1, int(input())+1):
    # 예약된 손님 수, M초동안 k개 생산 가능
    N, M ,K = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()
    print('#{} {}'.format(tc, jingi(N, M ,K, people)))



