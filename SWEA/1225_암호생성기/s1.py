import sys
sys.stdin = open('input.txt')

def Password(numbers):
    value = 1
    while numbers[len(numbers)-1] != 0:
        if numbers[0] - value > 0:
            numbers.append(numbers.pop(0)-value)
        else:
            numbers.pop(0)
            numbers.append(0)

        if value == 5:
            value = 1
        else:
            value += 1
    return numbers


while True:
    try:
        tc = input()
        numbers = list(map(int, input().split()))
        print('#{}'.format(tc), end=" ")
        print(*Password(numbers))
    except:
        break