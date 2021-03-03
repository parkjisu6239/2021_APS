def solution(priorities, location):
    # 중요도의 인덱스로 구성된 리스트 생성
    my_printer = [i for i in range(len(priorities))]

    i = 0
    # 반복문 내에서 pop, append 사용해서 for로 하면 인덱스 오류남
    while i < len(priorities):
        # 해당 인덱스의 다음 값부터 비교
        for j in range(i + 1, len(priorities)):
            # 현 인덱스의 우선순위보다 더 높은 우선순위가 있으면
            if priorities[i] < priorities[j]:
                # 현 인덱스를 제거하고 맨뒤로 넣어주고, break
                priorities.append(priorities.pop(i))
                my_printer.append(my_printer.pop(i))
                break
        # break 없이 반복문이 종료된 경우(i 인덱스의 우선순위가 제일 크다는 뜻)
        # i는 순서 변경이 필요없으니, 다음 인덱스로 넘어가면 됨
        else:
            i += 1

    # 최종적으로 리턴하는 결과는 내가 선택한 문서가 몇번째인지(1~n번째인지) 알아야 해서 +1
    return my_printer.index(location) + 1


print(solution([1, 1, 9, 1, 1, 1], 0))