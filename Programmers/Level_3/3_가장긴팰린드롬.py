def solution(s):
    # SWEA 문제
    # 가장 긴 팰린들롬부터 하나씩 낮춰가면서 확인

    # 팰린드롬의 길이
    for palin_len in range(len(s), 0, -1):
        # 확인할 시작 인덱스
        for i in range(len(s) - palin_len + 1):
            # 앞뒤 같은지 확인을 몇번 반복?
            for j in range(palin_len // 2):
                if s[i + j] == s[i + palin_len - 1 - j]:
                    continue
                else:
                    break
            else:
                return palin_len