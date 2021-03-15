def solution(n, t, m, p):
    # 맨 처음 0은 무조건 들어감, 그래서 숫자는 1부터
    result = '0'
    number = 1

    # 10 ~ 15는 알파벳으로 치환
    change = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

    # 튜브가 말해야 되는 숫자 다 나올 때까지
    while len(result) < t * m:
        temp = ''
        n_jin_num = number
        while n_jin_num > 0:
            # 10~15는 알파벳으로
            if str(n_jin_num % n) in change.keys():
                temp = change[str(n_jin_num % n)] + temp
            # 나머지는 그대로
            else:
                temp = str(n_jin_num % n) + temp
            n_jin_num //= n

        result += temp
        number += 1

    # 튜브가 말해야되는 갯수만큼 반복
    answer = ''
    i = 0
    while len(answer) < t:
        # 튜브 순서에만 결과에 넣기
        if i % m == p - 1:
            answer += result[i]
        i += 1
    return answer


print(solution(12, 16, 5, 2))