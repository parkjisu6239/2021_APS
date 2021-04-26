# 본인, 추천인, 판매자, 그 판매자가 판 수량
def solution(enroll, referral, seller, amount):
    result = {name: 0 for name in enroll}

    # 서로소 집합에서 부모 정보 초기화랑 동일 (크루스컬)
    p = dict()  # 부모 정보 (추천인)
    for i in range(len(enroll)):
        p[enroll[i]] = referral[i]
    p['-'] = '-'  # 다단계왕 민호는 자기자신이 부모

    # 판매자 순회
    for i in range(len(seller)):
        dadangye = amount[i] * 100  # 수익
        people = seller[i]

        while people != p[people] and dadangye > 0:
            result[people] += dadangye - dadangye // 10  # 수급할 돈 뺀 남은 돈
            dadangye //= 10  # 수급할 돈
            people = p[people]

    ans = []
    for name in enroll:
        ans.append(result[name])

    return ans


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))