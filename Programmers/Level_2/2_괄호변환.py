def solution(p):
    answer = ''

    # 1
    if p == '':
        return p

    # 2
    # 균형잡힌 괄호 이려면 일단 짝수임, p는 무조건 짝수길이로 주어짐
    u = ''
    v = ''
    if len(p) <= 2:
        u = p
    else:
        for i in range(2, len(p) - 1, 2):
            if p[0:i].count('(') == p[0:i].count(')'):
                u = p[0:i]
                v = p[i:]
                break

    # 3
    # 완벽한 괄호는 대칭되는 서로가 반대여야함
    if u[0] == '(' and u[-1] == ')':
        for i in range(len(u) // 2):
            if u[i] != u[len(u) - 1 - i]:
                continue
            else:
                break
        else:
            return u + solution(v)

    # 4
    # 위에서 완벽한 괄호가 아니라 break로 나온 경우
    u = u[1:-1]
    u = u.replace('(','a')
    u = u.replace(')', 'b')
    u = u.replace('a', ')')
    u = u.replace('b', '(')


    return '(' + solution(v) + ')' + u


print(solution("()))((()"))