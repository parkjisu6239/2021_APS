def solution(expression):
    # 연산자의 우선순위 경우의 수 6가지
    # 나머지는 계산기 풀이와 동일
    # 전위 > 후위 / 후위 > 계산 2단계가 아닌 한단계로 처리! 바로 계산!

    prioritys = [{'+': 1, '-': 2, '*': 3},
                 {'+': 1, '-': 3, '*': 2},
                 {'+': 2, '-': 1, '*': 3},
                 {'+': 2, '-': 3, '*': 1},
                 {'+': 3, '-': 1, '*': 2},
                 {'+': 3, '-': 2, '*': 1}
                 ]
    answer = 0
    for priority in prioritys:
        # 전위 표기식 > 후위 표기식
        num = [int(expression[0])]
        operator = []
        for i in range(1, len(expression)):
            # 피연산자
            if expression[i].isdigit():
                # 숫자가 연속해서 나온거면 수정
                if expression[i - 1].isdigit():
                    num.append(num.pop() * 10 + int(expression[i]))
                # 처음나온거면 그냥 추가
                else:
                    num.append(int(expression[i]))
            # 연산자
            else:
                # 비어있으면 추가
                if not operator:
                    operator.append(expression[i])
                else:
                    # 우선순위 높으면 추가
                    if priority[expression[i]] > priority[operator[-1]]:
                        operator.append(expression[i])
                    # 우선순위 낮으면
                    else:
                        # 높을때까지 기존에 쌓인거 빼서 num과 연산
                        while operator and priority[expression[i]] <= priority[operator[-1]]:
                            b = num.pop()
                            a = num.pop()
                            if operator[-1] == '+':
                                num.append(a + b)
                            elif operator[-1] == '-':
                                num.append(a - b)
                            else:
                                num.append(a * b)
                            operator.pop()
                        # 자리났으면 들어가기
                        operator.append(expression[i])

        # 끝나고 나면 연산자 남아있음, 없어질때까지 연산
        while operator:
            b = num.pop()
            a = num.pop()
            if operator[-1] == '+':
                num.append(a + b)
            elif operator[-1] == '-':
                num.append(a - b)
            else:
                num.append(a * b)
            operator.pop()

        # 최대값 갱신
        result = abs(num.pop())
        if result > answer: answer = result

    return answer


print(solution("100-200*300-500+20"))