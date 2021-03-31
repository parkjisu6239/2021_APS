# 짝수 = 짝수 + 짝수 > 이경우는 4 = 2+2 인 경우만 되고 6이상은 안된다(2가 아닌 짝수는 소수가 아님)
# 짝수 = 3이상의 홀수 + 3이상의 홀수
# 4이면 1, 그 이상의 짝수는 3이이상의 홀수 중에서 소수를 판단해야한다.

# 3이상의 홀수 + 3이상의 홀수 조합을 찾자

numbers = [0,0] + [1]* 999999

def prime():
    global numbers

    for i in range(2, 500001):
        if numbers[i] == 1:
            for j in range(2, 1000000//i+1):
                numbers[i*j] = 0

prime()

def partition(N):
    result = 0
    if N == 4:
        return 1

    for i in range(3, N // 2 + 1, 2):
        if numbers[i] and numbers[N-i]:
            result += 1

    return result


for _ in range(int(input())):
    N = int(input())
    print(partition(N))