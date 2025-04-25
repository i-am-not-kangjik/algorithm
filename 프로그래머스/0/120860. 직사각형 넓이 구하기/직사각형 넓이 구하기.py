def solution(dots):
    xs = [i[0] for i in dots]
    ys = [i[1] for i in dots]
    garo = abs(max(xs) - min(xs))
    sero = abs(max(ys) - min(ys))

    return garo * sero