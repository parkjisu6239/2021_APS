import sys
sys.stdin = open('input.txt')

def Card(S):
    # S, D, H, C 카드 정보
    card_idx = ['S', 'D', 'H', 'C']
    # 몇개가 필요한지 계산하기 위한 변수
    need_card_cnt = [13, 13, 13, 13]
    # 중복 카드를 확인하기 위한 변수
    card = [[], [], [], []]

    # 3개씩 카드 1개의 정보를 담고 있기때문에 step 3
    for i in range(0, len(S), 3):
        # 인덱스를 찾기
        for j in range(len(card_idx)):
            # 입력값과 같은 card_idx를 찾으면
            if S[i] == card_idx[j]:
                # 이미 이전의 데이터가 들어가 있으면 중복값인지 비교
                if len(card[j]) >= 1:
                    # card에 들어있는 데이터 중에서
                    for k in range(len(card[j])):
                        # 중복값이 있다면
                        if int(S[i + 1: i + 3]) == card[j][k]:
                            # 에러를 출력
                            return 'ERROR'
                # len(card[j])가 0이거나, 위에서 리턴 안되고(중복값 없어서) 아래로 내려온 경우
                # 그 카드번호를 card에 담고, 카드가 있는거니까 필요카드를 1개 빼기
                card[j].append(int(S[i + 1: i + 3]))
                need_card_cnt[j] -= 1


    return ' '.join(map(str, need_card_cnt))


for tc in range(1, int(input())+1):
    S = input()
    print('#{} {}'.format(tc, Card(S)))