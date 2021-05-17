def solution(gems):
    distinct = len(set(gems))
    result = []
    gem_dict = {}

    for idx, gem in enumerate(gems):
        gem_dict[gem] = idx
        if len(gem_dict) == distinct:
            result.append([min(gem_dict.values()) + 1, idx+1])

    result.sort(key = lambda x: (x[1] - x[0], x[0]))
    return result[0]



print(solution(["a", "b", "c", "d"]))
print(solution(["a", "a", "a"]))
print(solution(["a", "b", "a", "c", "b"]))
print(solution(['DIA', 'EM', 'EM', 'RUB', 'DIA']))
print(solution(	["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
