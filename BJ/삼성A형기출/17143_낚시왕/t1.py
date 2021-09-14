R, C = 2, 3

def move_shark(r, c, s, d):
    if d == 1: # 상
        if s <= r - 0:
            return r - s, c, d
        else:
           rd = s - r
           quo, remain = divmod(rd, R-1)
           if quo % 2 == 0: # 짝수번
               return remain, c, 2 if remain else 1
           else:
               return R-1-remain, c, 1 if remain else 2
    elif d == 2: # 하
        if s <= R-1-r:
            return r + s, c, d
        else:
            rd = s - (R-1-r)
            quo, remain = divmod(rd, R - 1)
            if quo % 2 == 0:  # 짝수번
                return R - 1 - remain, c, 1 if remain else 2
            else:
                return remain, c, 2 if remain else 1
    elif d == 3: # 우
        if s <= C-1-c:
            return r, c + s, d
        else:
            cd = s - (C-1-c)
            quo, remain = divmod(cd, C - 1)
            if quo % 2 == 0:  # 짝수번
                return r, C - 1 - remain, 4 if remain else 3
            else:
                return r, remain, 3 if remain else 4
    else: # 좌
        if s <= c - 0:
            return r, c-s, d
        else:
           cd = s - c
           quo, remain = divmod(cd, C-1)
           if quo % 2 == 0: # 짝수번
               return r, remain, 3 if remain else 4
           else:
               return r, C-1-remain, 4 if remain else 3


print(move_shark(1, 2, 5, 3))