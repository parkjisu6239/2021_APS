def solition(cookie):
    ans = 0

    for i in range(len(cookie)):
        cookie[i] += cookie[i-1]

    for end in range(len(cookie)-1, 0, -1):
        for pivot in range(len(cookie)-2, 0, -1):
            for start in range(len(cookie)-3, -1, -1):
                if cookie[end] - cookie[pivot] == cookie[pivot] - cookie[start]:
                    ans = max(ans, cookie[end] - cookie[pivot])
                elif cookie[end] - cookie[pivot] < cookie[pivot] - cookie[start]:
                    break

    return ans

print(solition([1,1,2,3,1,2,4,5]))