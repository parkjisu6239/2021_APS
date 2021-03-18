def solution(name):
    rename = [ (26 - (ord(n) - ord('A'))) if (ord(n) - ord('A')) > 13 else (ord(n) - ord('A')) for n in name]

    result = 0
    idx = 0
    while rename != [0] * len(name):
        result += rename[idx]
        rename[idx] = 0

        if rename == [0] * len(name):
            return result

        r,l = (1, 1)
        while rename[idx + r] == 0:
            r += 1

        while rename[idx - l] == 0:
            l += 1

        if l < r:
            result += l
            idx -= l
        else:
            result += r
            idx += r

    return result


print(solution("CANAAAAANAN"))