import sys
sys.stdin = open('eval_input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    card = list(input().split())
    new_card = []

    if N % 2:
        card_half_front = card[:N//2+1]
        card_half_back = card[N//2+1:]
        for i in range(N//2):
            new_card.append(card_half_front[i])
            new_card.append(card_half_back[i])
        new_card.append(card_half_front[-1])

    else:
        card_half_front = card[:N//2]
        card_half_back = card[N//2:]
        for i in range(N//2):
            new_card.append(card_half_front[i])
            new_card.append(card_half_back[i])

    print('#{}'.format(tc), end=" ")
    print(*new_card)
