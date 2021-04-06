def solution(genres, plays):
    genres_sum = dict()
    genres_info = dict()
    for i in range(len(genres)):
        # 장르별 총 플레이 수
        genres_sum[genres[i]] = genres_sum.get(genres[i], 0) + plays[i]
        # 정보 통합
        if genres[i] in genres_info.keys():
            genres_info[genres[i]].append([i, plays[i]])
        else:
            genres_info[genres[i]] = [[i, plays[i]]]

    # 플레이수로 장르 정렬
    genres_sum_list = []
    for key, val in genres_sum.items():
        genres_sum_list.append([val, key])
    genres_sum_list.sort(reverse=True)

    # 장르별 노래도 플레이스로 정렬
    for k in genres_info.keys():
        genres_info[k] = sorted(genres_info[k], key=lambda x: (-x[1], x[0]))

    answer = []
    for i in range(len(genres_sum_list)):
        genre = genres_sum_list[i][1]
        if len(genres_info[genre]) < 2:
            answer.append(genres_info[genre][0][0])
        else:
            answer.append(genres_info[genre][0][0])
            answer.append(genres_info[genre][1][0])

    return answer