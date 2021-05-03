def solution(s):
    answer = 0
    match = {'(':')', '[':']', '{':'}'}

    for i in range(len(s)):
        if i != 0:
            s = s[1:] + s[0]
        stack = []
        for ele in s:
            if ele in ('[', '(', '{'):
                stack.append(ele)
            else:
                if stack and match[stack[-1]] == ele:
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1

    return answer

print(solution("[["))