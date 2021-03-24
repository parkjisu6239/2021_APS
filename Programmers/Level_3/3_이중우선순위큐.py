def solution(operations):
    # 힙을 쓰거나, 매번 정렬을 해야하나? 시간초과될것 같다... 라고 생각했지만 아니었다.
    answer = []

    for operation in operations:
        operatior = operation.split()
        if operatior[0] == 'I':
            answer.append(int(operatior[1]))
        elif answer and operatior[0] == 'D':
            if operatior[1] == '1':
                answer.remove(max(answer))
            else:
                answer.remove(min(answer))

    if answer:
        return [max(answer), min(answer)]
    else:
        return [0, 0]


print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))