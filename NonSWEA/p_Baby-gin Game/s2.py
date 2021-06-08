import sys
sys.stdin = open("eval_input.txt", "r")


def babygin(numbers):
    # 0~9까지 숫자의 등장 횟수를 저장할 리스트 생성
    card_count = [ 0 for _ in range(10)]

    result = 0

    for number in numbers:
        card_count[number] += 1

    # 0~9까지 순회하면서, result를 구할 것
    i = 0
    while i < len(card_count):

        ###### run부터 쓰면 테케가 한개 실패함 왜??? #####
        ###### 111234 같은 경우 트리플릿부터 하면 1, 런부터 하면 0이 나옴, 최대로 되는걸 고르는거니까 1이 맞음 ######

        # triplet
        if card_count[i] >= 3:
            card_count[i] -= 3
            result += 1
            continue

        # run
        # 다음, 그 다음 인덱스 확인이 필요한데, 리스트 길이를 넘어서는 안되기때문에 i <= 7를 추가함
        # 만약 run이나 triplet에 해당 해서 아래와 같은 과정을 거치고 나면,
        # continue 가 없을때는 더 이상 해당 인덱스를 확인하지 않기 때문에 틀린 답이 나옴
        # 그래서 한번 더 수행하게 함
        if i < len(card_count) - 2:
            if card_count[i] and card_count[i + 1] and card_count[i + 2]:
                card_count[i] -= 1
                card_count[i+1] -= 1
                card_count[i+2] -= 1
                result += 1
                continue

        if result >= 2:
            return 1

        i += 1

    return 0


T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input()))
    print('#{} {}'.format(tc, babygin(numbers)))



