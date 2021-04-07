def solution(lines):
    times = []
    if len(lines) == 1:
        return 1

    for line in lines:
        infos = line.split()
        end_time = list(map(float, infos[1].split(':')))

        end = end_time[0] * 60 * 60 + end_time[1] * 60 + end_time[2]
        if end != 0:
            during = float(infos[2][:-1])
            start = round(end - during + 0.001, 3)
        else:
            start = 0.0
        times.append([start, end])

    print(times)

    rear, tail = int(times[0][0]), int(times[-1][1])
    max_request = 0
    for second in range(rear, tail+1):
        request = 0
        for time in times:
            if second <= time[0] <= second + 1:
                request += 1
            elif time[0] <= second < second + 1 <= time[1]:
                request += 1
            elif second <= time[1] <= second + 1:
                request += 1
        if request > max_request:
            max_request = request

    return max_request

print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))