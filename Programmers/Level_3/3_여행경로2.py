def solution(tickets):
    # 인접 딕셔너리
    fly = dict() # 노드 정보
    airports = set() # 공항들
    ticket_cnt = len(tickets) # 티켓 수

    for ticket in tickets:
        fly[ticket[0]] = fly.get(ticket[0], []) + [ticket[1]]
        airports.add(ticket[0])
        airports.add(ticket[1])

    n = len(airports) # 공항 수
    result = [] # 최종 결과
    path = [] # 경로 생성


    def DFS(s, cnt): # 시작점, 사용한 티켓 수
        path.append(s) # 시작점을 경로에 담는다

        if len(set(path)) == n and cnt == ticket_cnt: # 모든 공항을 방문 했고, 티켓 다 썻으면
            result.append(list(path)) # 경로를 결과에 추가
            return

        if s not in fly.keys(): # 더 가야되는데, s를 출발지로 하는 티켓이 없으면
            return # 리턴

        for i in range(len(fly[s])): # s를 출발지로 하는 티켓 중에서
            if len(fly[s][i]) == 3: # 아직 안쓴 티켓
                e = fly[s][i]
                fly[s][i] = 'Done' # 쓴것으로 표시
                DFS(e, cnt+1) # e로 출발하도록 ㄱㄱ

                # 함수 호출 끝나서 빠져나온 부분
                fly[s][i] = e # 티켓 원상복구
                path.pop() # 경로에서 제거

    DFS('ICN', 0) # 시작점, 사용한 티켓 수

    return sorted(result)[0]


print(solution([['ICN', 'BBB'], ['AAA', 'ICN'], ['ICN', 'AAA']]),"\n",['ICN', 'AAA', 'ICN', 'BBB'])
print(solution(	[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]),"\n",["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])