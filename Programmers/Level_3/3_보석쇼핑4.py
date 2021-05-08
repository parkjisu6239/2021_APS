def solution(gems):
    que_idx = []
    que_gem = []

    for i in range(len(gems)-1, -1, -1):
        if not que_idx:
            que_idx.append(i)
            que_gem.append(gems[i])
            continue

        if que_gem[0] == gems[i]:
            que_idx.pop(0)
            que_idx.append(i)
            que_gem.pop(0)
            que_gem.append(gems[i])

            while len(que_idx) >= 2 and que_gem[0] == que_gem[1]:
                que_idx.pop(0)
                que_gem.pop(0)
        else:
            que_idx.append(i)
            que_gem.append(gems[i])


    while que_gem and que_gem[-1] in que_gem[:-1]:
        que_gem.pop()
        que_idx.pop()


    return [que_idx[-1]+1, que_idx[0]+1]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(['DIA', 'EM', 'EM', 'RUB', 'DIA']))