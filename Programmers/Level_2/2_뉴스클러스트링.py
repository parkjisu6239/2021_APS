def solution(str1, str2):
    # 대소문자 구분X
    str1 = str1.lower()
    str2 = str2.lower()

    # 처음에는 리스트로 했다가
    # 자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장할 수 있다.
    # 이 내용 처리 하기 위해 dict로 구성
    str1_sub, str2_sub = dict(), dict()
    # 각각 2문자로 쪼개서 둘다 알파벳이면 넣고, 아니면 버린다
    for i in range(len(str1) - 1):
        if str1[i:i + 2][0].isalpha() and str1[i:i + 2][1].isalpha():
            str1_sub[str1[i:i + 2]] = str1_sub.get(str1[i:i + 2], 0) + 1
    for i in range(len(str2) - 1):
        if str2[i:i + 2][0].isalpha() and str2[i:i + 2][1].isalpha():
            str2_sub[str2[i:i + 2]] = str2_sub.get(str2[i:i + 2], 0) + 1

    # 둘다 공집합이면 65536 리턴 끝
    if not str1_sub and not str2_sub:
        return 65536

    # 교집합, 합집합 구한다. 갯수만 필요해서 정수로 받는다
    intersection = 0
    union = 0
    for key, val in str1_sub.items():
        # str1에 있는게 str2에도 있으면
        if key in str2_sub:
            # 교집합은 최소값, 합집합은 최대값(지문에서 그러라고 함)
            intersection += min(val, str2_sub[key])
            union += max(val, str2_sub[key])
        # str1에만 있으면 합집합에만
        else:
            union += val

    # 교집합은 위에서 이미 구해졌고, str2에만 있는걸 합집합에 넣기 위한 반복
    for key, val in str2_sub.items():
        if key not in str1_sub:
            union += val

    return int(intersection / union * 65536)


print(solution('E=M*C^2', 'e=m*c^2'))