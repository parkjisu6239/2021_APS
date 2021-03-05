def solution(s):
    # 패턴 검색! 패턴이 연속해서 n개 나온다면 압축은 n pattern으로 작성된다
    # 패턴이 확인되었다면 압축하고, 압축한 다음 인덱스로 넘어가서
    # 패턴이 하나도 발견되지 않았으면 바로 다음 인덱스로 넘어간다
    # 패턴의 길이는 전체 문장의 절반 이하이다.

    min_len = len(s)
    # 가능한 패턴의 길이만큼 반복
    for n in range(1, (len(s))//2 + 1):
        # 패턴 검사 인덱스 오류를 막고, 후처리를 쉽게 하기 위해 변형
        s_copy = s + ('#' * n)
        # 압축된 문자열
        zip_s = ''
        # 인덱스, 중복수
        i = 0
        cnt = 1
        while i < len(s):
            # 같은 경우
            if s_copy[i: i+n] == s_copy[i+n: i+ 2*n]:
                # 중복수 올리기
                i += n
                cnt += 1
            # 다른 경우
            else:
                # 중복횟수가 2이상이면
                if cnt != 1:
                    # 그 숫자 앞에 붙이고, 패턴붙이기
                    zip_s += str(cnt) + s_copy[i: i+n]
                    # cnt 원상복구
                    cnt = 1
                    i += n
                # 중복된거 없으면
                else:
                    # 숫자 없이 그 패턴만 붙이기
                    zip_s += s_copy[i: i+n]
                    i += n

        # 위경우를 거치면 모든 문자열이 압출 완료되지만, 뒤에 '#' 붙는 경우가 있음
        # 그래서 '#'제거하고 압축된 문자열만 남김
        zip_s = zip_s.replace('#'*zip_s.count('#'),'')

        # 최소길이라면 최소길이 갱신
        if len(zip_s) < min_len:
            min_len = len(zip_s)

    return min_len

print(solution("abcabcdede"))