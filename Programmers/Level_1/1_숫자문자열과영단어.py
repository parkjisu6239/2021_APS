def solution(s):
    answer = ''
    num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    temp = ''
    for i in s:
        if i.isalpha():
            temp += i
        else:
            if temp:
                answer += str(num[temp])
                temp = ''
            answer += str(i)

        if num.get(temp, -1) != -1:
            answer += str(num[temp])
            temp = ''

    return int(answer)

print(solution("one4seveneight"))