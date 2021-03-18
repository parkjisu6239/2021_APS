def solution(progresses, speeds):
    answer = []
    # 개발이 완료된(진도 100이상) 기능은 뺄거라서, 인덱스 오류가 안나는 while로 진행
    while len(progresses) > 0:
        # 각 기능에, 개발 속도를 더해줌(1일 경과)
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]

        # 맨앞 기능이 배포가 가능하면
        if progresses[0] >= 100:
            # 배포 가능한 기능 수를 1로 초기화, 배포 불가능한 기능의 index를 idx로 받을 것임
            cnt = 1
            idx = 0
            # 맨앞은 위 조건문에서 확인했으니, 1부터 끝까지 확인
            for j in range(1, len(progresses)):
                # 만약 동시에 배포가 가능한 기능이 있으면
                if progresses[j] >= 100:
                    # 배포기능수를 올리고, 다음 턴으로 넘어감
                    cnt += 1
                    continue
                # 배포불가능한 기능이 나오면, 그때의 인덱스를 저장하고, 반복을 멈춤(남은 기능들을 개발이 더 필요하므로)
                else:
                    idx = j
                    break
            # 만약 위 반복문을 모두 순회하고, break를 만나지 않았다면, 모든 기능이 배포 가능이라는 뜻
            # 위에서 구해진 최종 배포기능수를 결과에 추가하고, 리턴으로 종료함
            else:
                answer.append(cnt)
                return answer

            # 위 반복문에서 break로 종료된 경우, 아직 배포불가한 기능이 있는거고, 그 기능의 인덱스를 idx로 받아놨음
            # 일단 위에서 구한 배포가능한 기능 수를 결과에 추가하고
            answer.append(cnt)
            # 배포 가능한 기능외에, 불가능한 기능부터~끝까지를 새로 할당함, speed도 마찬가지
            progresses = progresses[idx:]
            speeds = speeds[idx:]

    return answer

print(solution( [93, 30, 55], [1, 30, 5]))