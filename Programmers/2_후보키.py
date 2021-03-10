def solution(relation):
    # 중복값이 없으면 고유키이기때문에 무조건 후보키!
    # 중복값이 있다면, 다른 컬럼과의 조합으로 후보키가 될 수 있다. >> 부분집합?
    # 그리고 n개 컬럼의 조합으로 최소 후보키가 된다면, 여기에 다른 컬럼을 추가한 것들은 후보키로 판단하지 않는다.
    answer = 0
    temp = []
    for idx, record in enumerate(zip(*relation)):
        if len(set(record)) == len(record):
            answer += 1
        else:
            temp.append(record)

    cadidate = list(zip(*temp))

    N = len(cadidate[0])
    sel = [0] * N
    candi_key_comb = []

    def subset(idx):
        nonlocal candi_key_comb
        if idx == N:
            if sum(sel) >= 2:
                ok = candidatekey(sel)
                if ok:
                    candi_key_comb.append(list(ok))
            return

        sel[idx] = 0
        subset(idx + 1)

        sel[idx] = 1
        subset(idx + 1)

    def candidatekey(sel):
        nonlocal answer
        iscadi = []
        for i, candi in enumerate(zip(*cadidate)):
            if sel[i]:
                iscadi.append(candi)
        if len(set(zip(*iscadi))) == len(list(zip(*iscadi))):
            return sel
        return

    subset(0)

    for i in range(len(candi_key_comb)-1):
        for j in range(i+1, len(candi_key_comb)):
            check = 0
            for k in range(len(candi_key_comb[i])):
                if candi_key_comb[i][k] + candi_key_comb[j][k] == 2:
                    check += 1
            if check == sum(candi_key_comb[i]):
                candi_key_comb.pop(j)

    return answer + len(candi_key_comb)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))