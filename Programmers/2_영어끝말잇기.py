def solution(n, words):
    stack = []
    who = 1  # 1번사람 ~ n 번사람
    turn = 1  # 현재가 몇번째 턴인지

    for word in words:
        # 스택이 비었다면(첫순서라면) 뭘 말하든 통과
        if not stack:
            stack.append(word)
            who += 1
        # 두번째부터, 이전사람이랑 중복된거 말한거 아니고, 끝말 잘 이었으면 통과
        elif word not in stack and stack[-1][-1] == word[0]:
            stack.append(word)
            who += 1
        # 통과하지 못하면 종료
        else:
            break

        # 현재 턴에서 n명이 모두 통과했으면
        if who > n:
            # 턴 올리고
            turn += 1
            # 1번사람으로 초기화
            who = 1

    # 종료되지 않고 모두 통과했다면 탈락자 없음
    else:
        return [0, 0]

    return [who, turn]