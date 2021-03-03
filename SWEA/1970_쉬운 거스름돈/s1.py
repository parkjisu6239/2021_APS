import sys
sys.stdin = open("input.txt", "r")

def change(money):
    # 거스름돈 리스트와 결과 리스트 생성
    changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0] * 8

    # 인덱스 조정을 위해 while문 이용
    i = 0
    while i < 8:
        # money가 현재 인덱스의 거스름돈 보다 커야 거슬러줄수 있음
        # 그래서 money가 더 작으면, 인덱스 다음으로 넘기기
        # 어차피 위에서 초기값을 모두 0으로 지정해서 결과에 더할필요 없음
        if money - changes[i] < 0:
            i += 1
        # 현재 인덱스의 거스름돈을 줄수 있는 경우
        else:
            # 거슬러줌, 거슬러준 금액 카운트 올리기
            money -= changes[i]
            result[i] += 1
            # 거슬러준 다음에 또 같은 금액 뺏을때
            # 그 돈을 거슬러줄수 없으면 인덱스를 높이고,
            # 한번더 거슬러 줄수 있으면 인덱스 올리지 말고 다음턴으로 넘기기
            if money - changes[i] < 0:
                i += 1
            else:
                continue

    return result

T = int(input())

for tc in range(1, T+1):
    money = int(input())
    print('#{}'.format(tc))
    # 거스름돈의 카운트가 int라서 join을 하기 위해서는 각 원소들이 str이어야함 그래서 아래처럼 바꿔줌
    print(" ".join(list(map(str, change(money)))))