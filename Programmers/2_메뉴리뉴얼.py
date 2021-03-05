def solution(orders, course):
    result = []

    for n in course:
        answer = {}
        for order in orders:
            order = ''.join(sorted(order))
            if len(order) > n:
                for i in range(1 << len(order)):
                    temp = ''
                    for j in range(len(order)):
                        if i & (1 << j):
                            temp += order[j]
                    if len(temp) == n:
                        answer[temp] = answer.get(temp, 0) + 1
            elif len(order) == n:
                answer[order] = answer.get(order, 0) + 1

        print(answer)
        temp_result = []
        for N in range(len(orders), 1, -1):
            if not temp_result:
                for key, val in answer.items():
                    if val == N: temp_result.append(key)
            else: break
        if temp_result: result.extend(temp_result)

    return sorted(result)

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))