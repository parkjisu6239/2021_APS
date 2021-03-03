import sys
sys.stdin = open("input.txt")

# 전구의 갯수
T = int(input())
# 전구의 상태
bubbles = list(map(int, input().split()))
# 학생수
students = int(input())

#학생수만큼 반복
for _ in range(students):
    # 성별과, 번호를 받음
    gender, number = map(int, input().split())

    # 남자면 번호의 배수를 상태변경
    if gender == 1:
        # 전구개수만큼 반복
        for i in range(T):
            # 번호는 1부터 시작해서 i+1을 확인함
            if (i+1) % number == 0:
                # 0은 1로 1은 0으로 바꾸라는 의미
                bubbles[i] = (bubbles[i] + 1)  % 2
    # 여자면 양옆 좌우 대칭인만큼 상태변경
    else:
        # 양옆 어디까지 대칭인지 볼 인덱스 j
        j = 1
        # 번호가 1부터라 -1로 인덱스화 해줌
        number -= 1
        # 내 기준 j만큼 왼쪽으로 간게 0이상이고 j만큼 오른쪽으로 간게 T-1 이하이면
        # 즉, 좌우가 인덱스를 넘어가지 않으면
        while number-j >= 0 and number+j <= T-1:
            # 양쪽이 다르면 멈추기
            if bubbles[number-j] != bubbles[number+j]:
                break
            # 같으면 그 다음 양옆을 확인하기 위해 j를 올려줌
            else:
                j += 1
        # 확인을 완료한 j는 양옆이 다르거나, 인덱스를 넘어가게 되어 반복문을 탈출한거라서
        # 그대로 사용하면 인덱스 오류가 뜨거나 결과가 다르기 때문에
        # 내가 원하는 조건에 맞는 j는 1을 빼야함
        j -= 1
        # 위에서 구한 j로 number 앞뒤 j까지의 전구상태를 바꿔줌
        for k in range(number-j, number+j+1):
            bubbles[k] = (bubbles[k] + 1) % 2

# 출력형식이 독특하네요.. 안읽고 풀었다가 틀려서 추가했습니다
while len(bubbles) >= 20:
    print(*bubbles[:20])
    bubbles = bubbles[20:]
print(*bubbles)

