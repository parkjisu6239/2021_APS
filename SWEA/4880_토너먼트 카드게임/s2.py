import sys
sys.stdin = open('input.txt')

# 1은 가위, 2는 바위, 3은 보
# 같은 카드인 경우 편의상 번호가 작은 쪽을 승자

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
    if len(people) == 1:
        return people[0]
    elif len(people) == 2:
        return Winner(people[0], people[1])
    else:
        # 앞쪽 절반
        front = RockPaperScissors(people[: (len(people)+1)//2])
        # 뒤쪽 절반
        back = RockPaperScissors(people[(len(people)+1)//2: ])
        # 앞뒤 우승자 가위바위보
        result = RockPaperScissors([front] + [back])
        return result


for tc in range(1, int(input())+1):
    N = int(input())
    card = list(map(int, input().split()))
    # 우승자가 몇번째 사람인지 출력해야해서 인덱스와 묶어서 리스트 생성
    people = []
    for i in range(len(card)):
        people.append([i+1, card[i]])
    print(people)
    print('#{} {}'.format(tc, RockPaperScissors(people)[0]))