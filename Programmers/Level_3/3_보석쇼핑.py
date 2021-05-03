# 부르트포스 시간초과
def solution(gems):
    distinct_gem = set(gems)
    G = len(distinct_gem)

    if len(gems) == G:
        return [1, len(gems)]

    for i in range(G, len(gems)+1):
        for start in range(len(gems)-i+1):
            if len(set(gems[start:start+i])) == G:
                return [start+1, start+i]

print(solution(["a", "b", "c", "d"]))
print(solution(["a", "a", "a"]))
print(solution(["a", "b", "a", "c", "b"]))
print(solution(['DIA', 'EM', 'EM', 'RUB', 'DIA']))
print(solution(	["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))