# N, K, M = map(int, input().split())

N, K, M = 5, 2, 3

people = list(range(1, N+1))
cnt = 0
num = 1
idx = 0

while True:
    if num == K:
        if people[idx] == M:
            print(cnt+1)
            break
        else:
            people.pop(idx)
            cnt += 1
            num = 1
            continue

    num += 1
    idx = (idx + 1) % len(people)

