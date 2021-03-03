def solution(numbers):
    numbers = list(map(str, numbers))
    for i in range(len(numbers)):
        for j in range(0, len(numbers)-1):
            if int(numbers[j] + numbers[j+1]) < int(numbers[j+1] + numbers[j]):
                numbers[j + 1], numbers[j] = numbers[j], numbers[j + 1]
    print(numbers)
    return ''.join(map(str, numbers))

print(solution([1,11,110,10,100,1000]))


