def solution(msg):
    answer = []
    # 사전에 사전 생성하기 ㅋ
    dictionary = {chr(alpha): alpha - 64 for alpha in range(65, 91)}
    # 새로 추가되는 단어 넘버링
    number = 27
    i = 0
    while i < len(msg):
        # 인덱스 늘리면서, 슬라이싱한 단어가 사전에 있는지 확인
        for j in range(len(msg) - i + 1):
            # 없으면 그만
            if msg[i: i + j + 1] not in dictionary.keys():
                break
        # 마지막 인덱스이면, 색인번호 출력
        if i == len(msg)-1:
            answer.append(dictionary.get(msg[i]))
            break
        else:
            # 단어의 색인 번호 출력
            answer.append(dictionary.get(msg[i: i + j]))
            # 새로운 단어 사전에 등록
            dictionary[msg[i: i + j + 1]] = number
            number += 1
            i += j

    #print(dictionary)
    return answer

print(solution('TOBEORNOTTOBEORTOBEORNOT'))