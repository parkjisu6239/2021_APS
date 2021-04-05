from itertools import combinations

def solution(relation):
    # 부분집합을 구한다.
    # 단, 최소성을 만족하기 위해서 A가 후보키이면 A의 멱집합들은 더이상 조회하지 않는다.

    # 1. 라이브러리로 원소의 갯수가 1개~필드수인 후보키 조합을 만든다
    combi = []
    for i in range(len(relation)):
        combi.extend(list(combinations(range(len(relation[0])), i)))
    #print(combi)

    # 2. 조합키가 후보키가 될 수 있는지 확인한다.
    result = 0
    candi_keys = []
    for i in range(1, len(combi)):

        # 조합(combi[i])이 후보키의 멱집합인 경우 최소성을 유지하기 위해 탐색 X
        skip = 1
        for candi in candi_keys:
            if set(candi).issubset(set(combi[i])):
                skip = 0
                break

        # 후보키의 멱집합이 아닌 경우
        if skip:
            # 전체 레코드를 담을 변수
            key = []
            for j in range(len(relation)):
                # j 행의 레코드를 담을 변수
                temp = []
                for k in range(len(relation[0])):
                    # 조합에 맞는 인덱스만
                    if k in combi[i]:
                        temp.append(relation[j][k])
                # 중복된 레코드가 있으면 후보키 X
                if temp in key:
                    break
                else:
                    key.append(temp)
            # break 없이 모두 고유한 레코드인 경우
            else:
                result += 1
                candi_keys.append(combi[i])

    #print(candi_keys)
    return result


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                    ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))