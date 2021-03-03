import sys
sys.stdin = open('input.txt', 'r', encoding = 'UTF-8')

def StringCounter(str1, str2):
    str1_dict = dict()
    # str1의 각 알파벳을 key로 가지는 dict 생성
    for str1_alpha in str1:
        str1_dict[str1_alpha] = 0

    # str2를 순회
    for str2_alpha in str2:
        # str2에 str1의 알파벳이 있으면 갯수 추가
        if str2_alpha in str1_dict.keys():
            str1_dict[str2_alpha] += 1

    # 최대값 찾기
    max_val = 0
    for val in str1_dict.values():
        if val > max_val:
            max_val = val

    return max_val

for tc in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    print('#{} {}'.format(tc, StringCounter(str1, str2)))