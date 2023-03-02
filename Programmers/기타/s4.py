
def solution(arr):
    arr.sort(key=lambda x: x[1])
    meeting = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i][0] < meeting[-1][1]:
            continue

        meeting.append(arr[i])

    return len(meeting)


print(solution([[1, 4], [2, 6], [4, 7]]))