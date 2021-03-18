def solution(files):
    # 정렬할 때 파일명을 수정할거라서, 원본파일을 백업해둠
    original_files, sorted_files = dict(), []
    for idx, file in enumerate(files):
        original_files[idx] = file
        # 헤드, 넘버, 테일 나누기
        head = '' # 글자로만 이루어진 맨앞부분
        number = '' # 숫자로만 이루어진 중간 부분
        tail = '' # 다시 숫자가 아닌 다른 문자가 나오기 시작하는 부분
        for i in range(len(file)):
            # 숫자가 나온적 없고, 숫자가 아니면 헤드 (처음부터 글자만 연속해 나오고 있다면)
            if not number and not file[i].isnumeric():
                head += file[i].lower()
            # 테일이 공백이고, 숫자이면 넘버(글자가 끝나고, 숫자가 연속해서 나오고 있다면)
            elif not tail and file[i].isnumeric():
                number += file[i]
            # 숫자가 채워진 후 글자가 나오면 테일(글자연속/숫자연속이 끝나고, 다시 처음 글자가 나온 이후)
            elif number and not file[i].isnumeric():
                tail += file[i].lower()
        sorted_files.append([idx, head, int(number)])
    #print(sorted_files)
    # 3개 정보에 대해 모두 사전순(오름차순) 정렬
    sorted_files = sorted(sorted_files, key=lambda x: (x[1], x[2], x[0]))
    answer = []
    for j in range(len(sorted_files)):
        answer.append(original_files[sorted_files[j][0]])
    return answer

print(solution(["foo010bar020.zip", "foo9.txt", "F-15", "img1.png", "IMG01.GIF", "img2.JPG"]))