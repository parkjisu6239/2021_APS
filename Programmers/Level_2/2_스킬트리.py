def solution(skill, skill_trees):
    answer = 0

    # 스킬트리 안에 있는 스킬들 순회
    for skill_tree in skill_trees:
        # 스킬트리에서 선행스킬의 인덱스를 담을 리스트 준비
        skill_idx = []
        # 선행스킬을 돌면서, 스킬트리에서 선행스킬이 있는 인덱스를 찾을 것임
        for i in range(len(skill)):
            for j in range(len(skill_tree)):
                # 선행스킬이 스킬트리에 있으면, 그때의 인덱스를 skill_idx에 추가하고, 순회 중지
                if skill[i] == skill_tree[j]:
                    skill_idx.append(j)
                    break
            # 선행스킬이 스킬트리에 없어서 중단되지 않고, 반복문이 완전히 종료되었다면
            else:
                # 인덱스를 100으로 지정함(스킬트리의 길이는 최대 26이라서, 그보다 큰수 아무거나로 지정하면됨)
                skill_idx.append(100)

        # 선행스킬의 인덱스를 모두 찾고 나면, 선행 스킬일수록 스킬트리에서의 인덱스가 더 작아야함
        for k in range(len(skill_idx) - 1):
            # 선행스킬인데 인덱스가 더 크면, 현재 스킬트리는 불가능하므로, break하여 다음 스킬트리를 찾음
            if skill_idx[k] > skill_idx[k + 1]:
                break
        # break 없이 반복문이 종료되면, 선행스킬의 인덱스가 오름차순으로 스킬트리를 잘 짠것이니
        # answer를 올려줌
        else:
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
