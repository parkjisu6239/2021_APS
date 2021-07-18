def solution(numbers, hand):
    # 거리는 유클리디안거리가 아니라 보스턴으로 구해야하는게 포인트!(상하좌우로만 움직일수있어서)
    # 왼쪽번호는 phone[0], 가운데번호는 phone[1], 오른쪽번호는 가운데번호는 phone[2] 인덱스로 접근할 예정

    answer = ''
    l_position = [0, 0]
    r_position = [2, 0]

    phone = [
        ['*', 7, 4, 1],
        [0, 8, 5, 2],
        ['#', 9, 6, 3]
    ]

    if hand == 'right':
        what_hand = 'R'
    else:
        what_hand = 'L'

    for number in numbers:
        # 눌러야할 번호가 왼쪽인경우
        if number in phone[0]:
            l_position = [0, phone[0].index(number)]
            answer += 'L'
        # 눌러야할 번호가 오른쪽인경우
        elif number in phone[2]:
            r_position = [2, phone[2].index(number)]
            answer += 'R'
        # 눌러야할 번호가 가운데인경우
        # 가까운 손 계산 필요
        else:
            # 눌러야할 번호의 y좌표 / x좌표는 1고정!(가운데숫자라)
            press_y = phone[1].index(number)
            # 왼손과의 거리(보스턴) : abs(l_position[0] - 1) + abs(l_position[1] - phone[1].index(number))
            l_distance = abs(l_position[0] - 1) + abs(l_position[1] - press_y)
            # 오른손과의 거리 : abs(r_position[0] - 1) + abs(r_position[1] - phone[1].index(number))
            r_distance = abs(r_position[0] - 1) + abs(r_position[1] - press_y)
            # 왼손이 가깝 > 왼손으로 누르셈
            if l_distance < r_distance:
                l_position = [1, press_y]
                answer += 'L'
            # 오른손이 가깝 > 오른손으로 누르셈
            elif r_distance < l_distance:
                r_position = [1, press_y]
                answer += 'R'
            # 두손 거리가 같다면
            else:
                # 어느손잡이인지에 따라 그 손으로 누르고
                if hand == 'right':
                    r_position = [1, press_y]
                else:
                    l_position = [1, press_y]
                # 어느 손잡이인지에 따라 위에서 처리해 둔걸로 결과에 더하기
                answer += what_hand

    return answer