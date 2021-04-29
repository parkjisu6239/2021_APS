def solution(user_id, banned_id):
    answer = [] # 중복 비교를 위해 조합 저장
    N = len(banned_id)
    sel = ['']*N
    visit = [0] * len(user_id)

    cnt = 0
    def Banned(idx):
        nonlocal cnt
        if idx == N:
            if set(sel) not in answer:
                cnt += 1
                answer.append(set(sel))
            return

        for u, user in enumerate(user_id):
            if len(banned_id[idx]) == len(user) and visit[u] == 0:
                for i in range(len(banned_id[idx])):
                    if banned_id[idx][i] != '*':
                        if banned_id[idx][i] == user[i]:
                            continue
                        else:
                            break
                else:
                    visit[u] = 1
                    sel[idx] = user
                    Banned(idx+1)
                    visit[u] = 0

    Banned(0)

    return cnt

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))