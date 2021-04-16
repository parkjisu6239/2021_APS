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
        times.append([int(start * 1000), int(end * 1000)])

    times.sort(key=lambda x: x[1])

    max_request = 0
    for target in times:
        s = target[1]
        e = target[1] + 1000
        request = 0
        for overlap in times:
            if s <= overlap[0] < e or s <= overlap[1] < e or overlap[0] <= s < e <= overlap[1]:
                request += 1
        if request > max_request:
            max_request = request

    return max_request

print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))