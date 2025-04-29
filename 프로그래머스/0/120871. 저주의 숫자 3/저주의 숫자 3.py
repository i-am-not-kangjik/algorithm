def solution(n):
    tmp = []
    i = 1
    while (len(tmp) < 100):
        if i % 3 != 0 and i % 10 != 3 and i // 10 != 3 and i // 10 % 10 != 3:
            tmp.append(i)
        i += 1

    return tmp[n-1]