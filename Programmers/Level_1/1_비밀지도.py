def solution(n, arr1, arr2):
    # < idea >
    # 9의 이진수 + 30의 이진수 이진수구할때는 나누어떨어질떄까지가 아니라 n 회 해야함
    # 각 수의 이진수 0,1을 리스트의 원소로 만들고 두 이진수 리스트를 더함
    # 만약 요소의 값이 0이 아니면 벽, 0이면 공백이라는 뜻
    # 그래서 출력결과를 뽑을때 '#' 인지 ' '인지나타냄

    answer = []
    for i in range(n):
        temp = ''
        for _ in range(n):
            temp_sum = 0
            if arr1[i] > 0 or arr2[i] > 0:
                if arr1[i] > 0:
                    temp_sum += arr1[i] % 2
                    arr1[i] //= 2
                if arr2[i] > 0:
                    temp_sum += arr2[i] % 2
                    arr2[i] //= 2
            else:
                temp_sum += 0

            if temp_sum:
                temp = '#' + temp
            else:
                temp = ' ' + temp
        answer.append(temp)
    return answer