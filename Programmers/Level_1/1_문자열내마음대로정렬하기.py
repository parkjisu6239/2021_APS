def solution(strings, n):
    answer = []
    words = []
    for string in strings:
        words.append([string[n], string])
    '''
    words.sort()

    for word in words:
        answer.append(word[1])

    return answer
    '''

    for i in range(len(words)):
        for j in range(i, len(words)):
            if words[i][0] > words[j][0]:
                words[i], words[j] = words[j], words[i]
            elif words[i][0] == words[j][0]:
                if words[i][1] > words[j][1]:
                    words[i], words[j] = words[j], words[i]

    for word in words:
        answer.append(word[1])

    return answer