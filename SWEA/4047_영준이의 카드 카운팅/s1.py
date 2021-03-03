import sys
sys.stdin = open('input.txt')

def Card(S):
    # S, D, H, C 카드 정보
    card_idx = ['S', 'D', 'H', 'C']
    card = [[], [], [], []]

    for i in range(0, len(S), 3):
        if int(S[i + 1: i + 3]) in card[card_idx.index(S[i])]:
            return 'ERROR'
        card[card_idx.index(S[i])].append(int(S[i + 1: i + 3]))

    need_card_cnt = [13, 13, 13, 13]
    for j in range(len(card)):
        need_card_cnt[j] -= len(card[j])

    return ' '.join(map(str, need_card_cnt))


for tc in range(1, int(input())+1):
    S = input()
    print('#{} {}'.format(tc, Card(S)))