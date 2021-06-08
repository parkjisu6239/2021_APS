import sys
import time
sys.stdin = open('eval_input.txt')
start = time.time()


def is_babygin(card):
    for i in range(len(card)):
        if card[i] >= 3:
            return True

        if i < 8 and card[i] >= 1 and card[i+1] >= 1 and card[i+2] >= 1:
            return True

    return False


for tc in range(1, int(input())+1):
    all_card = list(map(int, input().split()))
    A_cnt, B_cnt = [0] * 10, [0] * 10
    A, B = [0] * 6, [0] * 6

    win = 0
    for i in range(len(all_card)):
        # A 차례
        if i % 2 == 0:
            A[i // 2] = all_card[i]
            A_cnt[all_card[i]] += 1
            # 3장 이상 있으면 판별
            if i >= 4 and is_babygin(A_cnt):
                win = 1
                break
        # B 차례
        else:
            B[i // 2] = all_card[i]
            B_cnt[all_card[i]] += 1
            # 3장 이상 있으면 판별
            if i >= 4 and is_babygin(B_cnt):
                win = 2
                break

    print('#{} {}'.format(tc, win))


print((time.time() - start)*1000) # 0.9996891021728516