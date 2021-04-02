from bisect import bisect_left

def solution(info, query):
    answer = [0]*len(query)
    infos = [tuple(i.split()) for i in info]

    # 지원자 정보를 딕셔너리의 키로, 점수를 벨류로 저장
    # 여러개일 경우 점수 높은 순 정렬
    combination = dict()
    for info in infos:
        combination[info[:4]] = combination.get(info[:4], []) + [int(info[4])]
        if len(combination[info[:4]]) > 1:
            combination[info[:4]] = sorted(combination[info[:4]])

    # 쿼리 순회
    for idx, q in enumerate(query):
        # 질문에서 and, - 빼고 자르기
        temp = q.replace('and', '').replace('-', '').split()
        # 점수빼고 내용만 set으로 만들기
        resume = set(temp[:-1])
        # 점수
        score = int(temp[-1])
        # 전체 조합 + 지원자 조합
        for key in combination:
            if resume.issubset(set(key)):
                # 점수가 쿼리보다 높은 지원자 수만 세기
                answer[idx] += len(combination[key]) - (bisect_left(combination[key], score))

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))