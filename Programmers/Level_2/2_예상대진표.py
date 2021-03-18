def solution(n,a,b):
    people = [i for i in range(1, n+1)]
    answer = 0
    while True:
        # 우승자를 담을 스택
        stack = []
        # 토너먼트 수
        answer += 1
        # 둘씩
        for i in range(0, len(people), 2):
            # a,b 같이 있으면 여기까지 걸린 토너먼트 수 반환
            if a in people[i:i+2] and b in people[i:i+2]:
                return answer
            # a가 있으면 a가 우승자라고 하자
            elif a in people[i:i+2]:
                stack.append(a)
            # b가 있으면 b가 우승자라고 하자
            elif b in people[i:i+2]:
                stack.append(b)
            # 아니면 그냥 번호작은쪽이 이겼다고 하자
            else:
                stack.append(people[i])
        # 우승자가 다 구해졌으면, 그 사람들끼리만 싸우게 하자
        people = stack