def solution(m, musicinfos):
    # 일단 m 이 musicinfos과 일치하는(포함되는)지를 확인한다.
    # 재생시간(끝-시작) 만큼 노래가 반복된다. 그 반복되는 노래에 m이 포함되어 있으면 일치!
    # 일치하는게 여러개라면 재생시간이 긴것, 재생시간도 일치한다면, 먼저 나온 노래!

    # C# 같은건 c 로 바꿔줌
    i_heard = ''
    for i in range(len(m)):
        if m[i] == '#':
            i_heard = i_heard[:-1] + m[i-1].lower()
        else:
            i_heard += m[i]


    that_song = []
    for musicinfo in musicinfos:
        # 콤마기준으로 나누어서 각 정보들을 나누고
        start, end, title, content = musicinfo.split(',')
        # 시작시간, 끝시간도 시간/분으로 나눈다
        start_time = list(map(int, start.split(':')))
        end_time = list(map(int, end.split(':')))
        if end_time[0] == 0 and end_time[1] == 0:
            end_time = [23, 60]
        # 재생시간을 구한다
        runtime = start_time[0] * 60 + start_time[1] - end_time[0] * 60 + end_time[1]

        song = ''
        for con in content:
            if con == '#':
                song = song[:-1] + song[-1].lower()
            else:
                song += con

        song_loop = song*(runtime//len(song)) + song[:runtime%len(song)]

        #print(song, song_loop)
        if i_heard in song_loop:
            if not that_song:
                that_song = [runtime, title]
            elif runtime > that_song[0]:
                that_song = [runtime, title]


    if that_song:
        return that_song[1]
    else:
        return '(None)'


print(solution("C", ["03:00,03:06,FOO,AC#B", "04:00,04:01,BAR,CC#BCC#BCC#B"]))