def solution(slice, n):
    answer = 1
    while(n > slice):
        n -= slice
        answer += 1
    return answer