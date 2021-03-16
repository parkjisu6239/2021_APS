def solution(numbers):
    numbers = list(map(str, numbers))

    def quicksort(numbers):
        if len(numbers) < 2:
            return numbers

        pivot = 0
        left = []
        right = []

        for i in range(1, len(numbers)):
            if int(numbers[i] + numbers[pivot]) >  int(numbers[pivot] + numbers[i]):
                right.append(numbers[i])
            else:
                left.append(numbers[i])
        return  quicksort(right) + [numbers[pivot]] +  quicksort(left)

    return str(int(''.join(quicksort(numbers)))) # 00000을 0으로 하기 위해


print(solution([1, 10, 101, 0]))