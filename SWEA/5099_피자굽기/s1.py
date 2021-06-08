import sys
sys.stdin = open('eval_input.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    # 오븐 안에 들어있는 피자, 아직 밖에서 대기중인 피자
    Oven, wait = [], []

    # 출력을 위해 인덱스도 같이 저장
    for i in range(M):
        if i < N: Oven.append([i+1, cheese[i]])
        else: wait.append([i+1, cheese[i]])

    # 마지막 피자
    last_pizza = 0

    # 오븐에 피자가 있는 동안 반복
    while Oven:
        # 마지막에 있던 피자
        last_pizza = Oven[-1][0]

        # 반복문 내에서 pop, append로 길이가 바뀌어서 while로
        pizza = 0
        while pizza < len(Oven):
            # 치즈가 녹는다
            Oven[pizza][1] //= 2
            # 치즈가 다 녹으면
            if Oven[pizza][1] == 0:
                # 대기열에 피자가 있다면
                if wait:
                    # 맨앞 대기열 피자를 화덕에 넣는다
                    Oven[pizza] = wait.pop(0)
                    pizza += 1
                # 대기열에 피자가 없다면, 다 익은 피자만 꺼낸다
                else:
                    Oven.pop(pizza)
            else:
                pizza += 1

    print('#{} {}'.format(tc, last_pizza))
