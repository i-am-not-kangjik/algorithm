def solution(numlist, n):
    tmp = list(map(lambda x: [abs(x - n), x], numlist))
    tmp.sort(key = lambda x: (x[0], -x[1]))
    
    answer = [x[1] for x in tmp]
    return answer