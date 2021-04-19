def solution(tickets):
    # DFS, 방문한 곳을 또 방문할 수도 있다.

    # 인접 딕셔너리
    fly = dict()
    for ticket in tickets:
        fly[ticket[0]] = fly.get(ticket[0], []) + [ticket[1]]

    stack = ['ICN']
    path = []

    while stack:
        # 이동 경로 넣기
        start = stack.pop()
        path.append(start)

        # 더 이상 갈 곳이 없으면 경로 출력
        if fly.get(start, 0) == 0 or not fly[start]:
            return path

        # 종점 리스트, 사전순 앞쪽
        end_list = fly[start]
        end_list.sort()

        # 티켓 사용해서 비행기 타기
        stack.append(end_list.pop(0))



print(solution([['ICN', 'SFO'], ['SFO', 'ICN'], ['ICN', 'SFO'],['SFO', 'JFK']]), "\n",['ICN', 'SFO', 'ICN', 'SFO', 'JFK'])
print(solution([['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'],['A', 'C']]), "\n",['ICN', 'A', 'ICN', 'A', 'C'])
print(solution([['ICN', 'A'], ['A', 'ICN'], ['A', 'B'],['ICN', 'A']]), "\n",['ICN', 'A', 'ICN', 'A', 'B'])
print(solution([['ICN', 'BBB'], ['AAA', 'ICN'], ['ICN', 'AAA']]),"\n",['ICN', 'AAA', 'ICN', 'BBB'])
print(solution([['ICN', 'ABB'], ['AAA', 'ICN'], ['ICN', 'AAA'], ['ICN', 'ADD'], [ 'ABB', 'ICN']]), "\n",['ICN', 'AAA', 'ICN', 'ABB', 'ICN', 'ADD'])
print(solution([['ICN', 'AAA'], ['ICN', 'AAA'], ['AAA', 'ICN'],['AAA', 'CCC']]), "\n",['ICN', 'AAA', 'ICN', 'AAA', 'CCC'])