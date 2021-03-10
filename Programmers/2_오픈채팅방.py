def solution(record):
    # 누군가 들어오고 나간 정보
    enter_out = []
    # 유저 아이디(key), 닉네임(value)
    userid = dict()
    answer = []

    for i in range(len(record)):
        info = record[i].split(' ')
        if info[0] == 'Leave':
            enter_out.append([info[1], info[0]])
        elif info[0] != 'Change':
            enter_out.append([info[1], info[0]])
            userid[info[1]] = info[2]
        else:
            userid[info[1]] = info[2]

    for i in range(len(enter_out)):
        if enter_out[i][1] == 'Enter':
            message = '님이 들어왔습니다.'
        else:
            message = '님이 나갔습니다.'
        answer.append(userid[enter_out[i][0]] + message)

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))