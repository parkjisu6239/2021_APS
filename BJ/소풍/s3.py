# N, K, M = map(int, input().split())

N, K, M = 5, 2, 3
# (1) 2 3 4 5 > 1 (3) 4 5 > 1 3 (5) > (3) 5 > (3) > ''
# 탈락하는 사람 몇번째 사람? 2 > 3 > 1 > 2 > 1
cnt = 0
nth_out = K - N if K > N else K

while N > 1:
    # 탈락자가 동호이면 종료
    if nth_out == M:
        break
    # 탈락자가 동호보다 앞에 있으면 번호 땡기기
    elif nth_out < M:
        M -= 1

    # 탈락했으니까 사람수 -1, 횟수 +1
    N -= 1
    cnt += 1

    # 다음 탈락자는 ?
    if nth_out > N:
        nth_out = 1
    nth_out = nth_out + (K-1) - N if nth_out + (K-1) > N else nth_out + (K-1)

print(cnt + 1)









