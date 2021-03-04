import sys
sys.stdin = open('input.txt')

# 1은 가위, 2는 바위, 3은 보
# 같은 카드인 경우 편의상 번호가 작은 쪽을 승자
# 전체 그룹을 무조건 반으로 나눈다 ? 무승부인 경우는 모두가 승자인가??
# 무승부경우가 없다면 모든 반복은 2번만에 종료된다.
# 처음 절반을 나누면 우승자가 각각 1명씩, 총 2명이 나온다. 그 둘이 가위바위보 하면 최종 승자가 나온다.
# 재귀로 될듯? 퀵정렬처럼?

def Winner(a, b):
    if a[1] > b[1]:
        big = a
        small = b
    elif a[1] < b[1]:
        big = b
        small = a
    else:
        return a

    if big[1] - small[1] == 1:
        return big
    else:
        return small

def RockPaperScissors(people):
    if len(people) == 2:
        return Winner(people[0], people[1])[0]

    front = people[: (len(people)+1)//2] # 앞쪽 절반
    back = people[(len(people)+1)//2: ] # 뒤쪽 절반

    # 가위바위보 하기
    f_winner = []
    f_rsp = [0, 0, 0]
    for i in range(len(front)):
        if not f_winner:
            f_winner.append(front[i])
            f_rsp[f_winner[0][1]-1] = 1
        else:
            if f_winner[-1][1] != front[i][1]:
                f_winner.append(Winner(f_winner.pop(), front[i]))
                if not f_rsp[front[i][1] - 1]:
                    f_rsp[front[i][1] - 1] = 1
    if f_rsp == [1, 1, 1]:
        f_winner = front


    b_winner = []
    b_rsp = [0, 0, 0]
    for j in range(len(back)):
        if not b_winner:
            b_winner.append(back[j])
            b_rsp[b_winner[0][1] - 1] = 1
        else:
            if b_winner[-1][1] != back[j][1]:
                b_winner.append(Winner(b_winner.pop(), back[j]))
                if not b_rsp[back[j][1] - 1]:
                    b_rsp[back[j][1] - 1] = 1
    if b_rsp == [1, 1, 1]:
        b_winner = back

    return RockPaperScissors(f_winner+b_winner)


for tc in range(1, int(input())+1):
    N = int(input())
    card = list(map(int, input().split()))
    # 우승자가 몇번째 사람인지 출력해야해서 인덱스와 묶어서 리스트 생성
    people = []
    for i in range(len(card)):
        people.append([i+1, card[i]])
    print('#{} {}'.format(tc, RockPaperScissors(people)))