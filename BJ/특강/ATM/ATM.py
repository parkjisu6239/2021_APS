
N = 5
waiting = [3, 1, 4, 3, 2]
N = int(input())
waiting = list(map(int, input().split()))

waiting.sort()
time = 0
for i in range(len(waiting)):
    time += waiting[i] * (N-i)

print(time)