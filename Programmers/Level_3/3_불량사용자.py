def solution(user_id, banned_id):
    answer = []
    for banned in banned_id:
        temp = set()
        for user in user_id:
            if len(banned) == len(user):
                for i in range(len(banned)):
                    if banned[i] != '*':
                        if banned[i] == user[i]:
                            continue
                        else:
                            break
                else:
                    temp.add(user)

        answer.append(temp)

    cnt = 1
    re = set()
    for ans in answer:
        cha = ans - re
        if cha:
            cnt *= len(cha)
        re = re | ans

    return cnt

print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))