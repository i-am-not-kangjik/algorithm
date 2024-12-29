def solution(n):
    n = str(n)
    answer = 0
    
    for i in range(0, len(n)):
        answer += int(n[i])
    return answer