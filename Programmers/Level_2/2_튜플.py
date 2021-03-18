def solution(s):
    # 원소가 1개 뿐인것이 첫번째
    # 원소가 2개인거중에서 첫번째 뺀게 2번쨰
    # n번째도 같은 방법으로
    answer = []

    # 1. 스트링을 각각 나눠서 리스트로 만들기
    # n자리의 문자열 표현된 숫자를 int로 변환하는 방법이 포인트!
    arr = []
    temp = []
    for i in range(1, len(s) - 1):
        if s[i].isnumeric() and s[i - 1].isnumeric():
            temp[-1] = temp[-1] * 10 + int(s[i])
        elif s[i].isnumeric():
            temp.append(int(s[i]))
        elif s[i] == '}':
            arr.append(temp)
            temp = []
    # print(arr)

    # 2. 길이가 짧은 순서대로 원소를 뽑아서 result에 더하기
    for i in range(1, len(arr) + 1):  # 원소의 길이를 찾기 위함
        for j in range(len(arr)):  # 인덱스
            if not answer and len(arr[j]) == i:
                answer.append(arr[j][0])
                break
            elif len(arr[j]) == i:
                for k in range(len(arr[j])):
                    if arr[j][k] not in answer:
                        answer.append(arr[j][k])
                        break

    return answer


print(solution("{{20,111},{111}}"))
