def solution(cookie):
    ans = 0

    for i in range(1, len(cookie)):
        cookie[i] += cookie[i-1]

    for a in range(len(cookie)-1):
        for b in range(a, len(cookie)-1):
            for c in range(b+1, len(cookie)):
                if cookie[b] - cookie[a] == cookie[c] - cookie[b]:
                    ans = max(ans, cookie[b] - cookie[a])

    return ans

print(solution([1,1,2,3]))
print(solution([1,2,4,5]))