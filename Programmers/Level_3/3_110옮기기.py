def change(binary):
    cnt = 0
    while "110" in binary:
        binary = binary.replace("110", "", 1)
        cnt += 1

    while cnt > 0:
        if '111' in binary:
            insert_idx = binary.index('111')
            binary = binary[:insert_idx] + '110'*cnt + binary[insert_idx:]
            break
        else:
            for i in range(len(binary)-1, -1, -1):
                if binary[i] == '0':
                    binary = binary[:i+1] + '110' + binary[i+1:]
                    break
            else:
                binary = '110' + binary
            cnt -= 1

    return binary


def solution(s):
    answer = []
    for binary in s:
        answer.append(change(binary))
    return answer



print(solution(["1110","100111100","0111111010", "10111111100"]))
print('["1101", "100110110", "0110110111", "10110110111]')

print(solution(["1011110","01110","101101111010"]))
print('["1011011", "01101", "101101101101"]')