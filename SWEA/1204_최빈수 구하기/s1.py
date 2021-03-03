import sys
sys.stdin = open('input.txt')


for _ in range(1, int(input())+1):
    tc = int(input())
    score = list(map(int, input().split()))

    # 0점~ 100점 등장 횟수
    counter = [0] * 101

    # 학생수만큼 점수 세기
    for i in range(len(score)):
        counter[score[i]] += 1

    # 최빈값 구하기(여러개일 경우 큰값)
    frequent_idx = 0
    for i in range(101):
        if counter[i] >= counter[frequent_idx]:
            frequent_idx = i

    # 출력은 등장 횟수가 아니라, 가장 많이 등장하는 값! 을 출력 (counter의 인덱스)
    print('#{} {}'.format(tc, frequent_idx))

