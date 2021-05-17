"""
< two point algorithm >
시작점과 끝점을 두고 탐색을 진행한다.
이 문제에서는 모든 보석을 포함할때까지 끝점을 하나씩 더하며 탐색을 한다.

시작~끝 구간에 모든 보석 종류가 포함되면,
시작점을 뒤로 한칸씩 당기면서 여전히 모든 보석을 포함하는지 확인한다.

모든 보석을 포함하는 최소 구간이 정해지면 결과로 선택한다.
"""

def solution(gems):
    distinct = len(set(gems))
    gems_len = len(gems)
    s, e = 0, 0

    min_d = gems_len + 1
    result = []
    cart = {}

    while s < gems_len and e < gems_len:
        if cart.get(gems[e], 0):
            cart[gems[e]] += 1
        else:
            cart[gems[e]] = 1
        e += 1

        if len(cart) == distinct:
            while s < e:
                if cart[gems[s]] > 1:
                    cart[gems[s]] -= 1
                    s += 1

                elif e-s < min_d:
                    min_d = e - s
                    result = [s+1, e]
                    break
                else:
                    break

    return result


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(	["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(['DIA', 'EM', 'EM', 'RUB', 'DIA']))