def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack or stack[-1] != s[i]:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop()

    return 0 if stack else 1