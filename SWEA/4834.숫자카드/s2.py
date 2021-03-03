import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # 0~9카드 등장 횟수 저장
    card_cnt = [0] * 10
    N = int(input())
    numbers = list(map(int, input()))
    for number in numbers:
        card_cnt[number] += 1

    # 최댓값의 인덱스 찾기
    max_idx = 0
    for i in range(1, 10):
        if card_cnt[i] >= card_cnt[max_idx]:
            max_idx = i
    print('#{} {} {}'.format(tc, max_idx, card_cnt[max_idx]))