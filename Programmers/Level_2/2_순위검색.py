def solution(info, query):
    answer = []
    info = [list(i.split()) for i in info]
    query = [list((q.replace('and', '')).split()) for q in query]

    a = set([1,2, 3, 4,5])
    b = set([3,5])
    print(b.issubset(a))

    for i in range(len(query)):
        temp_cnt = 0
        for k in range(len(info)):
            for j in range(len(query[i])):
                if j < len(query[i]) - 1:
                    if query[i][j] == info[k][j] or query[i][j] == '-':
                        continue
                    else:
                        break
                else:
                    if int(info[k][j]) >= int(query[i][j]):
                        temp_cnt += 1
        answer.append(temp_cnt)
        
    return answer


print(solution(	["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))