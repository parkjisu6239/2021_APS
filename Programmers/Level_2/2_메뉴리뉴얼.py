def solution(orders, course):
    result = []

    # 만들 코스의 수만큼 반복
    for n in course:
        # 코스메뉴와 등장횟수를 담을 딕셔너리
        answer = {}
        # 주문수 만큼 반복
        for order in orders:
            # 정렬을 하지 않으면 AB, BA를 다른 코스로 저장해서 정렬함.
            # sorted를 쓰면 문자열이 리스트가 되서, join을 써서 다시 문자열로
            order = ''.join(sorted(order))
            # 주문내역보다 코스길이가 클때만 부분집합 구하기
            if len(order) > n:
                # 부분집합 구한다
                for i in range(1 << len(order)):
                    temp = ''
                    for j in range(len(order)):
                        if i & (1 << j):
                            temp += order[j]
                    # 부분집합을 다 구했을때, 부분집합 원소의 갯수가 코스의 수와
                    # 같아야지, 코스로 등록!
                    if len(temp) == n:
                        answer[temp] = answer.get(temp, 0) + 1
            # 주문수 = 코스 수이면, 그대로 한개만
            elif len(order) == n:
                answer[order] = answer.get(order, 0) + 1

        # 길이가 n인 코스들이 구해진 후에
        temp_result = []
        # 가장 많이 중복된 코스를 찾아야해서, 큰 값부터 순회
        for N in range(len(orders), 1, -1):
            # 중복 코스가 결정되지 않았을때만
            if not temp_result:
                # 주문횟수에 해당하는 코스를 결과에 추가
                for key, val in answer.items():
                    if val == N: temp_result.append(key)
            # 결과에 코스가 쌓이면 반복 중지
            else: break
        # 중복 코스가 구해졌으면, 최종 결과에 저장
        if temp_result: result.extend(temp_result)

    # 최종 결과는 정렬해서 출력
    return sorted(result)

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))