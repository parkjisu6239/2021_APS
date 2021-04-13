def solution(N, number):
    # 모든 사칙연산을 @라 하자
    # n=4일때 >> n=1경우@n=3경우 + n=2경우@n=2경우 + 'nnnn'
    # n=5일때 >> n=1경우@n=4경우 + n=2경우@n=3경우 + 'nnnnn'
    # n=6일때 >> n=1경우@n=5경우 + n=2경우@n=4경우 + n=3경우@n=3경우 + 'nnnnnn'
    # 따라서 n에 따라 그 결과들을 DP(memoization)을 사용하여 저장해야 한다.

    # n=1, 2인 경우는 피보나치에서 베이스 케이스 처럼 항상 자명하므로 미리 지정
    combination = [[N]]
    combination.append(list({N+N, N-N, N*N, 1, int(str(N)*2)}))
    # n을 사용한 횟수, len(combination)
    cnt = 2

    # 베이스 케이스인 경우 즉시 리턴
    if N == number:
        return 1
    elif number in combination[1]:
        return 2

    # N이 3개 이상 필요한 경우 반복
    while True:
        # 이번 반복에서 생성된 숫자를 담을 리스트
        temp = []
        # 짝 맞춰 사칙연산해주기 위함 (앞뒤앞뒤~)
        for i in range((cnt+1)//2):
            A, B = combination[i], combination[cnt-1-i]
            for a in A:
                for b in B:
                    # 짝궁 찾아 사칙연산
                    temp.append(a + b)
                    temp.append(a * b)
                    temp.append(a - b)
                    temp.append(b - a)
                    if a:
                        temp.append(b // a)
                    if b:
                        temp.append(a // b)
        # 연속된 숫자
        temp.append(int(str(N)*(cnt+1)))

        # 이번 턴에서 생성된 모든 숫자를 중복 없이 결과 리스트에 추가
        combination.append(list(set(temp)))

        # n을 한번 더 쓴것이니 +1
        cnt += 1

        # 만들어낸 숫자리스트에 타겟이 있으면 횟수 리턴
        if number in combination[cnt-1]:
            return cnt
        # 8번 넘었는데도 없으면 -1 리턴
        if cnt > 8:
            return -1



print(solution(5,12),4)
print(solution(2,11),3)
print(solution(5,5),1)
print(solution(5,10),2)
print(solution(5,31168),-1)
print(solution(1,1121),7)
print(solution(5,1010),7)
print(solution(3,4),3)
print(solution(5,5555),4)
print(solution(5,5550),5)
print(solution(5,20),3)
print(solution(5,30),3)
print(solution(6,65),4)
print(solution(5,2),3)
print(solution(5,4),3)
print(solution(1,1),1)
print(solution(1,11),2)
print(solution(1,111),3)
print(solution(1,1111),4)
print(solution(1,11111),5)
print(solution(7,7776),6)
print(solution(7,7784),5)
print(solution(2,22222),5)
print(solution(2,22223),7)
print(solution(2,22224),6)
print(solution(2,11111),6)
print(solution(2,11),3)
print(solution(2,111),4)
print(solution(2,1111),5)
print(solution(9,36),4)
print(solution(9,37),6)
print(solution(9,72),3)
print(solution(3,18),3)
print(solution(2,1),2)
print(solution(4,17),4)