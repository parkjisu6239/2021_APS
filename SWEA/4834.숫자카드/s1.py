import sys
sys.stdin = open("eval_input.txt", "r")

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    numbers = list(map(int, input()))
    card_count = [ 0 for _ in range(10)]

    # 카드의 등장 횟수를 저장
    for number in numbers:
        card_count[number] += 1

    # 카드의 최대 등장횟수 초기화
    max_card_cnt = 0

    # 카드등장 횟수의 최댓값과, 그때의 인덱스(카드번호)를 뽑음
    for card_num, card_cnt in enumerate(card_count):
        if card_cnt >= max_card_cnt:
            max_card_cnt = card_cnt
            max_card_num = card_num

    print('#{} {} {}'.format(tc, max_card_num, max_card_cnt))