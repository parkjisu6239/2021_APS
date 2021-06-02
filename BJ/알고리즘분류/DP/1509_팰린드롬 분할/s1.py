import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a = input()
n = len(a)

dp = [[0 for i in range(n + 1)]for j in range(n + 1)]
result = [sys.maxsize] * (n+1)
result[0] = 0

for i in range(1, n+1): # 한글자는 무조건 팰린드롬
    dp[i][i] = 1

for i in range(1, n): # 두글자이고, 같으면 팰린드롬
    if a[i-1] == a[i]:
        dp[i][i+1] = 1

for i in range(2, n): # j번째~i번째 문자중
    for j in range(1, n+1-i):
        if a[j-1] == a[j+i-1] and dp[j+1][i+j-1] == 1: # 양끝이 같고, 안쪽이 팰린드롬이면 팰린드롬
            dp[j][i+j] = 1

for i in range(1, n+1):
    result[i] = min(result[i], result[i-1] + 1)
    # result[i-1]+1인 이유는 result[i-1]까지의 팰린드롬에 j부터 i까지의 팰린드롬 한개를 더하는 것이기 때문이다
    for j in range(i+1, n+1):
        if dp[i][j]:
          # 팰린드롬이면
            result[j] = min(result[j], result[i-1] + 1)

print(result, result[n])
