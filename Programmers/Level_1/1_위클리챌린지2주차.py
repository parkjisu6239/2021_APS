def solution(scores):
    answer = ''
    n = len(scores)

    for idx, score in enumerate(zip(*scores)):
        avg = 0
        score = list(score)
        my = score[idx]
        score.sort()
        if (my == score[0] and score[1] == score[0]) or (my == score[-1] and score[-1] == score[-2]):
            total = sum(score) / n
        else:
            total = (sum(score) - my) / (n - 1)

        if total >= 90:
            answer += 'A'
        elif total >= 80:
            answer += 'B'
        elif total >= 70:
            answer += 'C'
        elif total >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer